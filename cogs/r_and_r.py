from discord.ext import commands

class Routine_and_Reminders(commands.Cog)
    def __init__(self,bot):
        self.bot = bot

    @task.loop(seconds=3)
    async def reminders():
        pass
    
    @commands.command(name = 'areminder')
    async def set_reminder(self,ctx):
        #any custom reminders, pass in params to set
        pass

    @commands.command(name = 'lreminder')
    async def list_reminders(self,ctx):
        pass

    @commands.command(name = 'rreminder')
    async def remove_reminder(self,ctx):
        pass

    @commands.command(name = 'aroutine')
    async def set_routine(self,ctx):
        #predefined routines, react to set routine
        pass


    @commands.command(name = 'lroutine')
    async def list_routines(self,ctx):
        pass

    @commands.command(name = 'rroutine')
    async def remove_routines(self,ctx):
        pass

    
    @commands.command()
    async def t(self,ctx):
        await ctx.
    
   


def setup():
    bot.add_cog(basic(bot))
def setup(bot):
    bot.add_cog(Routine_and_Reminders(bot))