import discord
from discord.ext import commands
from datetime import datetime
from db import db_methods

params = db_methods.config()
cur = db_methods.methods(params)

class data(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def init(self,ctx):
        #initialize user account
        user_id = ctx.author.id
        res = cur.initialize(user_id)
        if res:
            await ctx.send(f"{ctx.author.mention}, your account has been created!")
        else:
            await ctx.send("You already have an account!")

    @commands.command(name = 'survey')
    async def survey(self,ctx):
        # survey on overall
        # included in routines
        pass

    @commands.command(name = 'chart')
    async def chart(self,ctx):
        # chart of the data from survey
        pass

    @commands.command(name = 'stats')
    async def stats(self,ctx, topic = ''):
        # stats for a specific 'topics'
        pass

    @commands.command(name = 'profile')
    async def user_profile(self,ctx):
        # overall user profile
        pass

    @commands.command(name = 'leader')
    async def leaderboard(self,ctx, topic = ''):
        # leaderboard on a specific "topic"
        # included in routines
        pass




def setup(bot):
    bot.add_cog(data(bot))
