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
            await ctx.send(f"{ctx.author.mention}, you already have an account!")




    @commands.command(name = 'stats')
    async def user_stats(self,ctx, topic = ''):
        # general or specific stats for a user'
        user = cur.is_user()
        if not user:
            await ctx.send("You don't have an account yet, `.init` to create one!")
            return None

        pass

'''
    @commands.guild_only()
    @commands.command(name = 'leader')
    async def leaderboard(self,ctx, topic = ''):
        # leaderboard on a specific "topic"
        # included in routines
        pass



    @commands.command(name = 'survey')
    async def survey(self,ctx):
        # survey on overall
        # included in routines
        pass

    @commands.command(name = 'chart')
    async def chart(self,ctx):
        # chart of the data from survey
        pass
'''

def setup(bot):
    bot.add_cog(data(bot))
