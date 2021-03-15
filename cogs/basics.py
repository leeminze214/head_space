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
        await ctx.send(embed = embed)

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'Pong! In {round(bot.latency*1000, 2)} ms')

    
    @commands.command(name = 'q')
    async def motivational_quote(self,ctx):
        
        r = requests.get("https://type.fit/api/quotes")
        res = r.json()
        quote = res[random.randint(0,len(res)-1)]
        embed = discord.Embed()
        embed.title = "Quote"
        if quote["author"] != None:
            embed.description = f'"*{quote["text"]}*" ---{quote["author"]}'
        else:
            embed.description = f'"{quote["text"]}"'
        await ctx.send(embed=embed)

    
        

# @commands.command(name = 'res')
# async def resources_for(self,ctx, topic):
#     pass


# @commands.command(name = 'cute')
# async def cute_pictures(self,ctx):
#     pass
    

def setup(bot):
    bot.add_cog(basic(bot))
