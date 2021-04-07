import datetime as dt
from db.methods import methods


class user_data:

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
            methods.basic_commit([query1,query2,query3])
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
        res = methods.basic_fetch(query,'one')
        return res





user = user_data()

