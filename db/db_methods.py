import psycopg2
import json

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

params = config()
test = methods(params)
test.connect()
