from discord.ext import commands
import discord
import requests
import random



class basic(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed()
        embed.title = "help command"
        await ctx.send(embed = embed)

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'Pong! In {round(self.bot.latency*1000, 2)} ms')

    @commands.command(name = 'q')
    async def motivational_quote(self,ctx):
        r = requests.get("https://type.fit/api/quotes")
        res = r.json()
        quote = res[random.randint(0,len(res)-1)]
        embed = discord.Embed()
        
        if quote["author"] != None:
           embed.title = f'*"{quote["text"]}"* ---{quote["author"]}'
        else:
             embed.title = f'*"{quote["text"]}"*'
        await ctx.send(embed=embed)



        

# @commands.command(name = 'res')
# async def resources_for(self,ctx, topic):
#     pass

    


def setup(bot):
    bot.add_cog(basic(bot))
