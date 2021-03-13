from discord.ext import commands

class basic(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'Pong! In {round(bot.latency*1000, 2)} ms')


def setup(bot):
    bot.add_cog(basic(bot))
