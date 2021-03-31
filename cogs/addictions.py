import discord
from discord.ext import commands
from datetime import datetime
from db import db_methods
from decorators import decorrs as dec

params = db_methods.config()
cur = db_methods.methods(params)

class addictions(commands.Cog):

    @dec.is_user(addictions)
    @commands.command(aliases=['a','addiction'])
    async def addictions(self,ctx):
        print('after')
        #Lists all possible addictions
        pass

    @commands.command()
    async def user_addictions(self,ctx):
        #Lists user addictions
        pass

    @commands.command()
    async def add_addictions(self,ctx):

        pass

    @commands.command()
    async def remove_addiction(self,ctx, addiction = ""):
        pass

    @commands.command()
    async def reset_addictions(self,ctx, addiction =""):
        pass

def setup(bot):
    bot.add_cog(addictions(bot))