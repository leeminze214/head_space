from discord.ext import commands,tasks
class Routine_and_Reminders(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @tasks.loop(seconds=3)
    async def routines():
        #routines
        pass
    
    @commands.command(name = 'croutine')
    async def add_custom_routine(self,ctx):
        #add custom routine
        pass

    @commands.command(name = 'aroutine')
    async def add_general_routine(self,ctx):
        #predefined routines, react to set routine
        pass


    @commands.command(name = 'myroutine')
    async def list_routines(self,ctx):
        pass

    @commands.command(name = 'rroutine')
    async def remove_routine(self,ctx):
        pass

    @commands.command(name = 'eroutine')
    async def edit_rountine(self,ctx):
        pass

    
   



def setup(bot):
    bot.add_cog(Routine_and_Reminders(bot))