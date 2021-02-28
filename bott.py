import discord
import time
from discord.ext import commands,tasks

bot = commands.Bot(command_prefix='$')
water_id = 815637250527592491

@tasks.loop(hours=1.0)
async def water():
    chann = bot.get_channel(water_id)
    await chann.send("drink water!!!")
    
@bot.event
async def on_ready():
    print('logged in as {0.user}'.format(bot))
    water.start()
@bot.command()
async def test(ctx):
    await ctx.send('hi')
    
  

bot.run('ODE1MzI2ODk3NzAxMTI2MTg0.YDqyWA.981jNBre2JTDZ19h0RcHLJuflq4',bot=True)

