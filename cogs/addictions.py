import discord
from discord.ext import commands
from datetime import datetime
from db import db_methods
from my_decors.is_user_decor import is_user

params = db_methods.config()
cur = db_methods.methods(params)

class addictions(commands.Cog):

    @commands.command(aliases=['a','addiction'])
    @is_user
    async def addictions(self,ctx):
        await ctx.send('here are all the addictions')
        #Lists all possible addictions
        

    @commands.command()
    @is_user
    async def user_addictions(self,ctx):
        #Lists user addictions
        pass

    @commands.command()
    @is_user
    async def add_addictions(self,ctx):

        pass

    @commands.command()
    @is_user
    async def remove_addiction(self,ctx, addiction = ""):
        pass

    @commands.command()
    @is_user
    async def reset_addictions(self,ctx, addiction =""):
        pass

def setup(bot):
    bot.add_cog(addictions(bot))