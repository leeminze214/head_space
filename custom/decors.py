import asyncio
import functools
from db.methods import execute as ex

def is_user(func):
    @functools.wraps(func)
    async def wrapped(*args, **kwargs):
        ctx = args[1]
        user = ex.is_user(ctx.author.id)
        if not user:
            await ctx.send(f"{ctx.author.mention} you don't have an account yet, `.init` to create one!")
            return None
        #if user then execute called function
        return await func(*args, **kwargs)
    return wrapped

    
    