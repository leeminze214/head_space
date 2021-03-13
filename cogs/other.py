from discord.ext import commands



# @commands.command(name = 'motivation')
# async def motivation(self,ctx):
#     #included in routines
#     pass

# @commands.command(name = 'res')
# async def resources_for(self,ctx, topic):
#     pass


# @commands.command(name = 'cute')
# async def cute_pictures(self,ctx):
#     pass


class other(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def ot(self,ctx):
        await ctx.send("ot worked")


def setup(bot):
    bot.add_cog(other(bot))