from discord.ext import commands

# @commands.command(name = 'survey')
# async def survey(self,ctx):
#     #included in routines
#     pass

# @commands.command(name = 'stats')
# async def stats(self,ctx):
#     pass

# @commands.command(name = 'chart')
# async def chart(self,ctx, topic='all'):
#     pass

class data(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def dt(self,ctx):
        await ctx.send("dt worked")


def setup(bot):
    bot.add_cog(data(bot))
