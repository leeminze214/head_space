import discord
from discord.ext import commands,tasks


bot = commands.Bot(command_prefix='.', help_command = None)
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
    
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency,2)}ms.')

bot.run('ODE1MzI2ODk3NzAxMTI2MTg0.YDqyWA.981jNBre2JTDZ19h0RcHLJuflq4',bot=True)

