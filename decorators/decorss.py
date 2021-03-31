from db import db_methods

params = db_methods.config()
cur = db_methods.methods(params)

def is_user(func):
    # user = cur.is_user()
    # if not user:
    #     await ctx.send("You don't have an account yet, `.init` to create one!")
    #     return None
    print('before')
    func()