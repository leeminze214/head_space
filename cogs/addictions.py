import discord
from discord.ext import commands
from datetime import datetime
from db.methods import execute as ex
from custom.decors import is_user
from custom.valid_addictions import valid_addictions



class addictions(commands.Cog):

    @commands.command(aliases=['a','addiction'])
    @is_user
    async def addictions(self,ctx):
        '''
            list all addictions and current number of users that have each addiction
        '''
        addictions = ex.all_addictions()
        embed = discord.Embed()
        embed.title = "Addictions"  
        for i in addictions:
            addiction = i[0]
            number_of_users_addicted = ex.count_users_addicted(addiction)
            format_addiction = addiction[0].upper()+addiction[1:]
            embed.add_field(name = format_addiction, value = number_of_users_addicted, inline=True)
        await ctx.send(embed=embed)
        
        

    @commands.command(aliases=['ma'])
    @is_user
    async def user_addictions(self,ctx):
        #Lists user current addictions
        res = ex.fetch_user_addictions(ctx.author.id)
        print(res)
        #[[x,[x,x,x], [y,[y,y,y]]]
        if not res:
            await ctx.send(f'{ctx.author.mention}, you have no addictions kept in track!')
        
        else:
            embed = discord.Embed()
            embed.title = f'{ctx.author.name}\'s Addictions'
            embed.add_field(name = res[0][0],value= res[0][1] )
            await ctx.send(embed=embed)



    @commands.command(aliases=['aa'])
    @is_user
    async def add_addictions(self,ctx,addiction=''):

        if addiction in valid_addictions:
            res = ex.add_addiction(ctx.author.id,addiction)
            if res is not None:
                await ctx.send(f'{ctx.author.mention}, you are already keeping track of {addiction} addiction!')
            else:
                await ctx.send(f'{ctx.author.mention}, you are now keeping track of {addiction} addiction!')
                
        elif not len(addiction):
            embed = discord.Embed()
            embed.title = "ALL OF THEM add"
            await ctx.send(embed=embed)
        
        else:
            await ctx.send(f'{ctx.author.mention}, could not find {addiction} addiction!')




    @commands.command(aliases=['ra'])
    @is_user
    async def remove_addiction(self,ctx,addiction =''):

        if addiction in valid_addictions:
            stats = ex.remove_addiction(ctx.author.id,'gaming')
            if not stats:
                await ctx.send(f'{ctx.author.mention}, {addiction} is not being keep track of yet!')
            else:
                embed = discord.Embed()
                embed.title = f'Results'
                embed.add_field(name = 'Days', value = stats[0])
                await ctx.send(f'{ctx.author.mention}, your {addiction} addiction has been removed')
                await ctx.send(embed = embed)
                
        elif not len(addiction):
            embed = discord.Embed()
            embed.title = "ALL OF THEM remove"
            await ctx.send(embed=embed)
        
        else:
            await ctx.send(f'{ctx.author.mention}, could not find {addiction} addiction!')



    @commands.command()
    @is_user
    async def reset_addictions(self,ctx, addiction =""):
        pass


def setup(bot):
    bot.add_cog(addictions(bot))