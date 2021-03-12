import discord
from discord.ext import commands,tasks
import datetime as dt

token = str(open('tok.txt').read())
bot = commands.Bot(command_prefix='.', help_command = None)

##
##@task.loop(seconds=3)
##async def reminders():
##    


@bot.event
async def on_ready():
    print('logged in as {0.user}'.format(bot))

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! In {round(bot.latency*1000, 2)} ms')

@bot.command(name = 'areminder')
async def set_reminder(ctx):
    #any custom reminders, pass in params to set
    pass

@bot.command(name = 'lreminder')
async def list_reminders(ctx):
    pass

@bot.command(name = 'rreminder')
async def remove_reminder(ctx):
    pass

@bot.command(name = 'aroutine')
async def set_routine(ctx):
    #predefined routines, react to set routine
    pass


@bot.command(name = 'lroutine')
async def list_routines(ctx):
    pass

@bot.command(name = 'rroutine')
async def remove_routines(ctx):
    pass

@bot.command(name = 'motivation')
async def motivation(ctx):
    #included in routines
    pass

@bot.command(name = 'survey')
async def survey(ctx):
    #included in routines
    pass

@bot.command(name = 'stats')
async def stats(ctx):
    pass

@bot.command(name = 'chart')
async def chart(ctx, topic='all'):
    pass

@bot.command(name = 'res')
async def resources_for(ctx, topic):
    pass


@bot.command(name = 'cute')
async def cute_pictures(ctx):
    pass

@bot.command()
async def help(ctx):
    pass
bot.run(token,bot=True)
