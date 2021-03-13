from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def testing(self,ctx):
        await ctx.send('cogs worked')
        
def setup(bot):
    bot.add_cog(Greetings(bot))
