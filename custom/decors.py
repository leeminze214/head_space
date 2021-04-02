import asyncio
import functools
from apis.user import user

def is_user(func):
    @functools.wraps(func)
    async def wrapped(*args, **kwargs):
        ctx = args[1]
        user_exist = user.is_user(ctx.author.id)
        if not user_exist:
            await ctx.send(f"{ctx.author.mention} you don't have an account yet, `.init` to create one!")
            return None
        #if user then execute called function
        return await func(*args, **kwargs)
    return wrapped

    
    