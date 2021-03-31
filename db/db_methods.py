import psycopg2
import json
from datetime import datetime

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
        """Connect to a Postgres database."""
        if self.conn is None:
            self.conn = psycopg2.connect(
                host=self.host,
                user=self.username,
                password=self.pw,
                database=self.db,
            )
            print('database connected')
    

    def is_user(self,user_id):
        '''
            check if user is in db
        '''
        self.connect()
        cur = self.conn.cursor()
        query = f'SELECT EXISTS(SELECT 1 FROM user_info WHERE id=\'{user_id}\') '
        cur.execute(query)
        res = cur.fetchone()[0]
        cur.close()
        print(f'{user_id} in DB: {res}')
        return res


    def initialize(self, user_id):
        '''
        if user not in db, initialize an account
        '''
        is_user = self.is_user(user_id)
        if not is_user:
            cur = self.conn.cursor()
            query =f'''
                            INSERT INTO user_info(id)
                            VALUES('{user_id}')
                        '''
            cur.execute(queury)
            self.conn.commit()
            cur.close()
            print(f"{user_id} account has been initialized")
            return True
        print(f"{user_id} already has an account")
        return False

    

    
params = config()
test = methods(params)
test.connect()
