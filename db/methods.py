import psycopg2
import json
import datetime as dt
from custom.valid_addictions import valid_addictions

def config():
    with open('db/db_auth.json', 'r') as config:
        params = json.load(config)
    return params

class methods:

    def __init__(self, config):
        self.host = config['host']
        self.username = config['user']
        self.pw = config['password']
        self.db = config['database']
        self.conn = None
        


    def connect(self):
        if self.conn is None:
            self.conn = psycopg2.connect(
                host=self.host,
                user=self.username,
                password=self.pw,
                database=self.db,
            )
            print('database connected')
    


    def basic_fetch(self,query, fetchtype = '', size = None):
        self.connect()
        cur = self.conn.cursor()
        cur.execute(query)
        res = None
        if fetchtype == 'all':
            res = cur.fetchall()
        elif fetchtype == 'many':
            res = cur.fetchmany(size)
        else:
            res = cur.fetchone()
        cur.close()
        return res
            


    def basic_commit(self,query):
        self.connect()
        cur = self.conn.cursor()
        if type(query) == list:
            for q in query:
                cur.execute(q)
        else:
            cur.execute(query)
        self.conn.commit()
        cur.close()



    def initialize(self, user_id):
        '''
            Initializes an account for user
        '''

        is_user = self.is_user(user_id)
        if not is_user:
            query1 =f'''
                            INSERT INTO user_info(id)
                                VALUES({user_id})
                        '''
            query2 =f'''
                            INSERT INTO user_addictions(id)
                                VALUES({user_id})
                        '''
            query3 = f'''
                            INSERT INTO user_routines(id)
                                VALUES({user_id})
                        '''
            self.basic_commit([query1,query2,query3])
            return True
        #if user already has account
        return False

        

    def is_user(self,user_id):
        '''
            check if user is in db
            returns a bool
        '''

        query = f'''
                    SELECT EXISTS(SELECT 1 FROM user_info 
                        WHERE id = {user_id}) 
                '''
        res = self.basic_fetch(query,'one')[0]
        return res



#------------------------addictions------------------------------#
##
    def count_users_addicted(self, addiction):
        '''
            fetches number of users with
             <addiction> addiction
        '''

        query = f'''
                    SELECT COUNT({addiction}) FROM user_addictions
                        WHERE {addiction} IS NOT NULL;
                '''
        res = self.basic_fetch(query,'one')[0]
        return res
    

##
    def add_addiction(self, user_id, addiction):
        '''
            inserts addiction into user 
            account to keep track of
        '''

        time_now = dt.datetime.now()
        res = self.fetch_addiction(user_id,addiction)
        if res is None:
            update_query = f'''
                            UPDATE user_addictions
                                SET {addiction} = '{str(time_now)}'
                                    WHERE id = {user_id};
                            '''
            self.basic_commit(update_query)
            return True
        #already has addiction
        return False
           

##
    def fetch_addiction(self,user_id,addiction):
        '''
            fetches specific addiction start time
            return format is '%Y-%m-%d %H:%M:%S.%f'
        '''

        query = f'''
                    SELECT {addiction} FROM user_addictions
                        WHERE id = {user_id};
                '''
        res = self.basic_fetch(query, 'one')[0]
        return res



    def convert_str_time_to_datetime(self,str_time):
        '''
            converts time in string to datetime object
            return format '%Y-%m-%d %H:%M:%S.%f'

        '''

        time_format = '%Y-%m-%d %H:%M:%S.%f'
        time = dt.datetime.strptime(str_time,time_format)
        return time


##
    def fetch_user_addictions(self,user_id):
        '''
            fetches user's current addictions
            returns [ [addiction1, [d,h,m,s]], [addiction2, [d,h,m,s]].. ]
        '''

        valid = ''
        for i in valid_addictions:
            valid +=f'{i}, '
        query = f'''
                    SELECT {valid[:-2]} FROM user_addictions
                        WHERE id = {user_id};
                '''
        addiction_start_times = self.basic_fetch(query,'one')
        addiction_and_delta_times = []
        for time in zip(valid_addictions,addiction_start_times):
            if time[1] is not None:
                deltatime = self.addiction_results(user_id,start_date = time[1])
                addiction_and_delta_times.append([time[0],self.convert_dt_to_list(deltatime)])
        return addiction_and_delta_times



    def convert_dt_to_list(self,date):
        '''
            converts a time difference into a 
            list to access, returns [d,h,m,s]
        '''

        values = str(date).split()
        days = 0
        all_values = values[-1].split(':')
        all_values[-1] = all_values[-1][:2]
        if len(values)>1:
            days = values[0]
        all_values.insert(0, days)
        return all_values



##
    def remove_addiction(self,user_id,addiction):
        '''
            remove addiction from user account
            returns datetime list by self.convert_dt_to_list(date)
            or False
        '''
        diff = self.addiction_results(user_id,addiction=addiction)
        if bool(diff):
            #diff format: x days, h:m:s.f
            rep_time = diff.total_seconds()
            all_values = self.convert_dt_to_list(diff)
            query = f'''
                        UPDATE user_addictions 
                            SET {'s'+addiction} = array_append({'s'+addiction},{rep_time}), {addiction} = null
                                 WHERE id = {user_id};
                    '''
            self.basic_commit(query)
            return all_values
        return False



    def addiction_results(self,user_id,addiction=False,start_date = False):
        end = dt.datetime.now()
        start = None
        if bool(start_date):
            start = start_date
        else:
            start = self.fetch_addiction(user_id,addiction) 

        if start is not None:
            start = self.convert_str_time_to_datetime(start)
            return end-start
        return False




config = config()
execute= methods(config)
