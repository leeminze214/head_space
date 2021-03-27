import discord
from discord.ext import commands,tasks



token = str(open('tok.txt').read())
bot = commands.Bot(command_prefix='.', help_command = None)

initial_extensions = ["cogs.basics","cogs.user_data","cogs.daily_routines","cogs.addictions"]

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
        print('logged in as {0.user}'.format(bot))

bot.run(token,bot=True)
