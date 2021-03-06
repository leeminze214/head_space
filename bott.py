import discord
from discord.ext import commands,tasks
import datetime as dt

token = str(open('tok.txt').read())
bot = commands.Bot(command_prefix='.', help_command = None)

initial_extensions = ["cogs.basics","cogs.data","cogs.r_and_r","cogs.other"]

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
        print('logged in as {0.user}'.format(bot))

bot.run(token,bot=True)
