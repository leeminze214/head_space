import datetime as dt
from db.methods import methods
from custom.refers import valid_addictions


class addictions:
##
    def count_users_addicted(self, addiction):
        '''
            fetches number of users with
             <addiction> addiction
             returns fetched results
        '''

        query = f'''
                    SELECT COUNT({addiction}) FROM user_addictions
                        WHERE {addiction} <> 'None' AND {addiction} IS NOT NULL;
                '''
        res = methods.basic_fetch(query,'one')
        return res
    

##
    def add_addiction(self, user_id, addiction):
        '''
            inserts addiction into user 
            account to keep track of
            returns boolean 
        '''

        time_now = dt.datetime.now()
        res = self.fetch_addiction(user_id,addiction)
        if str(res) =='None':
            update_query = f'''
                            UPDATE user_addictions
                                SET {addiction} = '{str(time_now)}'
                                    WHERE id = {user_id};
                            '''
            methods.basic_commit(update_query)
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
        res = methods.basic_fetch(query, 'one')
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
        #optimize query
        valid = ''
        for i in valid_addictions:
            valid +=f'{i}, '
        query = f'''
                    SELECT {valid[:-2]} FROM user_addictions
                        WHERE id = {user_id};
                '''
        
        addiction_start_times = methods.basic_fetch(query,'all')
        addiction_start_times = addiction_start_times[0]
        addiction_and_delta_times = []
        for time in zip(valid_addictions,addiction_start_times):
            if str(time[1]) != 'None':
                deltatime = self.time_diff_results(time[1])
                addiction_and_delta_times.append([time[0],self.convert_dt_to_list(deltatime)])
        return addiction_and_delta_times



    def convert_dt_to_list(self,date):
        '''
            converts a time difference 'd day, h:m:s' 
            into a list to access, returns [d,h,m,s]
        '''

        values = str(date).split()
        days = 0
        if len(values)>1:
            days = values[0]
        all_values = values[-1].split(':')
        all_values[-1] = all_values[-1][:2]
        for i in range(1,3):
            if all_values[i][0] == '0':
                all_values[i] =  all_values[i][1]
        all_values.insert(0, days)
        return all_values



##
    def update_addiction(self,user_id,addiction,action = ''):
        '''
            removes or resets addiction
            updates database and appends new run
            returns runtime in list [d,h,m,s] and runtime in seconds (float)
        '''

        diff = self.addiction_time_results(user_id,addiction=addiction)
        if not diff:
            return False
        
        #diff format: x days, h:m:s.f
        addiction_time_now = None
        if action == 'remove':
            pass
        elif action == 'reset':
            addiction_time_now = str(dt.datetime.now())
        query = f'''
                    UPDATE user_addictions 
                        SET {'s'+addiction} = array_append({'s'+addiction},'{str(diff)}'), {addiction} = '{addiction_time_now}'
                                WHERE id = {user_id};
                '''
        methods.basic_commit(query)
        return diff

##
    def leader_boards(self,addiction):
        '''
            fetches leaders in an addiction
        '''

        query =f'''
                SELECT id,{addiction} FROM user_addictions
                    WHERE {addiction} <> 'None' AND {addiction} IS NOT NULL
                        ORDER BY {addiction} ASC
                            LIMIT 10
                '''
        a = methods.basic_fetch(query,'all')
        # leaders = []
        # for i in a:
        #     user = ctx.bot.get_user(i[0])

        #     leaders.append()
        return a

    def personal_best(self,user_id,addiction,record):
        '''
            checks whether record is a personal best
            returns boolean
        '''

        query = f'''
                    WITH records as(
                        SELECT unnest({'s'+addiction}) AS {'s'+addiction} FROM user_addictions
                    )
                    SELECT max({'s'+addiction}) FROM records;
                '''
        a = methods.basic_fetch(query,'one')
        #record is dt.timedelta type
        if str(record) == a:
            return True
        return False
        


    def addiction_time_results(self,user_id,addiction=False):
        '''
            calculates deltatime after user resets or removes addiction
            returns deltatime 'x days, h:m:s.f'
        '''
        
        start = self.fetch_addiction(user_id,addiction) 
        if str(start) == 'None':
            return False
        deltatime = self.time_diff_results(start)
        return deltatime



    def time_diff_results(self,start):
        '''
            takes in str_time and converts to datetime
            returns deltatime 'x days, h:m:s.f'
        '''

        end = dt.datetime.now()
        start = self.convert_str_time_to_datetime(start)
        return end-start
        



    

adic = addictions()
