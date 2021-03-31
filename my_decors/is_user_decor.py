import asyncio
import functools
from db import db_methods

params = db_methods.config()
cur = db_methods.methods(params)

def is_user(func):
    @functools.wraps(func)
    async def wrapped(*args, **kwargs):
        ctx = args[1]
        user = cur.is_user(ctx.author.id)
        print(user)
        if not user:
            await ctx.send("You don't have an account yet, type `.init` to create one!")
            return None
        #if user then execute called function
        return await func(*args, **kwargs)
    return wrapped

    
    