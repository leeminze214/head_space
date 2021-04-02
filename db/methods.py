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

    def all_addictions(self):
            '''
                fetches all addictions names
                 from db
            '''

            query ='''
                        SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
                            WHERE TABLE_NAME = 'user_addictions';
                    '''
            res = self.basic_fetch(query,'all')[1::2]
            return res
    


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
        else: 
            #already have addiction
            return False
           


    def fetch_addiction(self,user_id,addiction):
        '''
            fetches specific addiction start time
        '''

        query = f'''
                    SELECT {addiction} FROM user_addictions
                        WHERE id = {user_id};
                '''
        start = self.basic_fetch(query, 'one')[0]
        return start



    def convert_str_time(self,str_time):
        '''
            when time in string is fetched out of db
             use this to convert to datetime
        '''

        time_format = '%Y-%m-%d %H:%M:%S.%f'
        time = dt.datetime.strptime(str_time,time_format)
        return time



    def fetch_user_addictions(self,user_id):
        '''
            fetches user's current addictions
        '''
        ###works when only one addictions being returned from query############################################
        ###one result = ('x',)
        ###more = ("('x'),",)
        query = f'''
                    SELECT ({str(valid_addictions)[2:-2]}) FROM user_addictions
                        WHERE id = {user_id};
                '''
        ###goal: addiction_start_times = [timeres1,timeres2,timeres3]
        addiction_start_times = self.basic_fetch(query,'one')
        end = dt.datetime.now()
        addiction_and_delta_times = []
        for time in zip(valid_addictions,addiction_start_times):
            try:
                ###rn is it trying to convert something thats not a valid time
                
                deltatime = end-self.convert_str_time(time[1])
                addiction_and_delta_times.append([time[0],self.convert_dt_to_list(deltatime)])
            except:
                #time is null, meaning user does not have this addiction
                pass
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




    def remove_addiction(self,user_id,addiction):
        '''
            remove addiction from user account
        '''

        end = dt.datetime.now()
        start = self.fetch_addiction(user_id,addiction)
        if start is not None:
            start = self.convert_str_time(start)
            diff = end - start
            rep_time = diff.total_seconds()
            #diff format: x days, h:m:s.f
            all_values = self.convert_dt_to_list(diff)
            query = f'''
                        UPDATE user_addictions 
                            SET {'s'+addiction} = array_append({'s'+addiction},{rep_time}), {addiction} = null
                                 WHERE id = {user_id};
                    '''
            self.basic_commit(query)
            return all_values
        else:
            return False






config = config()
execute= methods(config)
