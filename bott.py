import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def auto_fish(message):
    if message.content.startswith('.f'):
        time.sleep(4680)
        await message.channel.send('.f')
'''
@client.event
async def react_to(message):
    if messsage.author == 'Big Tuna#3562":
        await message.add_reaction('')
'''
  

client.run('ODE1MzI2ODk3NzAxMTI2MTg0.YDqyWA.981jNBre2JTDZ19h0RcHLJuflq4')

