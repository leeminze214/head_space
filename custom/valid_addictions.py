'''
from db.methods import execute as ex

columns = self.all_addictions()
valid_addictions = [column[0] for column in columns if column[0] != 's' or column != 'id']
'''
valid_addictions = ['gaming','tobacco']