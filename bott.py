import discord
from discord.ext import commands,tasks


token = str(open('tok.txt').read())
bot = commands.Bot(command_prefix='.', case_insensitive=True,help_command = None)

initial_extensions = ["cogs.basics","cogs.user_data","cogs.daily_routines","cogs.addictions"]#,"cogs.misc"]

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
        print('logged in as {0.user}'.format(bot))

@bot.event
async def on_member_join(member):
        #current test ID
        sober_server_id = 812777619342753792
        if member.guild.id != sober_server_id:
                return None

        channel = member.guild.system_channel
        if channel is not None:
                await channel.send(f'Welcome to Sober {member.mention}!')
        role = discord.utils.get(member.guild.roles, name="Sober")
        await member.add_roles(role)




bot.run(token,bot=True)
