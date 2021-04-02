from discord.ext import commands,tasks
from custom.decors import is_user

class Routine_and_Reminders(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @tasks.loop(seconds=3)
    @is_user
    async def routines():
        #routines
        pass
    
    @commands.command(name = 'croutine')
    @is_user
    async def add_custom_routine(self,ctx):
        #add custom routine
        pass

    @commands.command(name = 'aroutine')
    @is_user
    async def add_general_routine(self,ctx):
        #predefined routines, react to set routine
        pass


    @commands.command(name = 'myroutine')
    @is_user
    async def list_routines(self,ctx):
        pass

    @commands.command(name = 'rroutine')
    @is_user
    async def remove_routine(self,ctx):
        pass

    @commands.command(name = 'eroutine')
    @is_user
    async def edit_rountine(self,ctx):
        pass

    
   



def setup(bot):
    bot.add_cog(Routine_and_Reminders(bot))

    '''
    import datetime

a = '2014-05-06 12:00:56'
b = '2013-03-06 16:08:22'

start = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
ends = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')

diff = start - ends

hours = int(diff.seconds // (60 * 60))
mins = int((diff.seconds // 60) % 60)'''