import discord
from discord.ext import commands
from datetime import datetime
from db.methods import execute as ex
from custom.decors import is_user
from custom.funcs import embed_time,string_time
from custom.refers import valid_addictions, time_names



class addictions(commands.Cog):

    @commands.command(aliases=['addictions','a'])
    async def list_all_addictions(self,ctx,only_list = False):
        '''
            list all addictions and current number 
            of users that have each addiction
            returns as embed
        '''
        
        embed = discord.Embed()
        embed.title = "Addictions"  
        for i in valid_addictions:
            addiction = i
            number_of_users_addicted = ex.count_users_addicted(addiction)
            format_addiction = addiction[0].upper()+addiction[1:]
            embed.add_field(name = format_addiction, value = number_of_users_addicted, inline=True)
        if only_list:
            return embed
        elif ex.is_user(ctx.author.id):
            await ctx.invoke(ctx.bot.get_command('add_addictions'))
        else:
            await ctx.send(embed=embed)
        
        

    @commands.command(aliases=['lista','la','laddictions','listaddictions'])
    @is_user
    async def list_user_addictions(self,ctx):
        #Lists user current addictions
        res = ex.fetch_user_addictions(ctx.author.id)
        #[[x,[x,x,x], [y,[y,y,y]]]
        if not res:
            await ctx.send(f'{ctx.author.mention}, you have no addictions kept in track!')
        
        else:
            embed = discord.Embed()
            embed.title = f'{ctx.author.name}\'s Addictions'
            for i in res:
                value = string_time(embed,i[1])
                embed.add_field(name = i[0],value= value)
            await ctx.send(embed=embed)



    @commands.command(aliases=['aa','addaddiction','adda'])
    @is_user
    async def add_addictions(self,ctx,addiction=''):
        if addiction in valid_addictions:
            res = ex.add_addiction(ctx.author.id,addiction)
            if res:
                await ctx.send(f'{ctx.author.mention}, you are now keeping track of {addiction} addiction!')
            else:
                await ctx.send(f'{ctx.author.mention}, you are already keeping track of {addiction} addiction!')

        
        elif not len(addiction):
            #react to add_addiction specific addiction
            embed = await ctx.invoke(ctx.bot.get_command('list_all_addictions'), only_list=True)
            await ctx.send(embed=embed)
        
        else:
            await ctx.send(f'{ctx.author.mention}, could not find {addiction} addiction!')




    @commands.command(aliases=['ra','removea','removeaddiction'])
    @is_user
    async def remove_addiction(self,ctx,addiction =''):

        if addiction in valid_addictions:
            res = ex.remove_addiction(ctx.author.id,addiction)
            #res is [d,h,m,s]
            if not res:
                await ctx.send(f'{ctx.author.mention}, {addiction} is not being keep track of yet!')
            else:
                embed = discord.Embed()
                embed.title = f'Results for {addiction} addiction'
                embed_time(embed,res)
                await ctx.send(f'{ctx.author.mention}, your {addiction} addiction has been removed')
                await ctx.send(embed = embed)
                
        elif not len(addiction):
            #react to remove_addiction specific addiction
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