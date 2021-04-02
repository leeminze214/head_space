import psycopg2
import json

def config():
    with open('db/db_auth.json', 'r') as config:
        params = json.load(config)
    return params

class db_methods:

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

config = config()
methods= db_methods(config)