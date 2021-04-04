import discord
from discord.ext import commands
from datetime import datetime
from apis.user import user
from apis.adic import adic
from custom.decors import is_user
from custom.funcs import embed_time,string_time
from custom.refers import valid_addictions, time_names



class addictions(commands.Cog):

    @commands.command(aliases=['addictions','a'])
    async def list_all_addictions(self,ctx):
        '''
            list all addictions and current number 
            of users that have each addiction
            returns as embed
        '''
        
        embed = discord.Embed()
        embed.title = "Addictions"  
        addictions_embeded = self.embed_all_addiction(embed)
        await ctx.send(embed = addictions_embeded)



    @commands.command(aliases=['lista','la','laddictions','listaddictions'])
    @is_user
    async def list_user_addictions(self,ctx):
        res = adic.fetch_user_addictions(ctx.author.id)
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
        addiction = addiction.lower()
        if addiction in valid_addictions:
            res = adic.add_addiction(ctx.author.id,addiction)
            if res:
                await ctx.send(f'{ctx.author.mention}, you are now keeping track of {addiction} addiction!')
            else:
                await ctx.send(f'{ctx.author.mention}, you are already keeping track of {addiction} addiction!')
        elif not len(addiction):
            #react to add_addiction specific addiction
            embed = discord.Embed()
            addicitons_embeded = self.embed_all_addiction(embed)
            #embed_emoji
            await ctx.send(embed=embed)
        else:
            await ctx.send(f'{ctx.author.mention}, could not find {addiction} addiction!')




    @commands.command(aliases=['ra','removea','removeaddiction'])
    @is_user
    async def remove_addiction(self,ctx,addiction =''):
        addiction = addiction.lower()
        if addiction in valid_addictions:
            res = adic.update_addiction(ctx.author.id,addiction,action='remove')
            #res is [d,h,m,s]
            if not res:
                await ctx.send(f'{ctx.author.mention}, {addiction} is not being keep track of yet!')
            else:
                embed = discord.Embed()
                embed.title = f'Results for {addiction} addiction - removed'
                embed_time(embed,res)
                await ctx.send(f'{ctx.author.mention}, your {addiction} addiction has been removed')
                await ctx.send(embed = embed)
        elif not len(addiction):
            #react to remove_addiction specific addiction
            embed = discord.Embed()
            embed.title = "ALL OF THEM remove"
            #embed_emoji
            await ctx.send(embed=embed)
        else:
            await ctx.send(f'{ctx.author.mention}, could not find {addiction} addiction!')



    @commands.command(aliases=['reset'])
    @is_user
    async def reset_addictions(self,ctx, addiction =""):
        addiction = addiction.lower()
        if addiction in valid_addictions:
            res = adic.update_addiction(ctx.author.id,addiction,action='reset')
            #res is [d,h,m,s]
            if not res:
                await ctx.send(f'{ctx.author.mention}, {addiction} is not being keep track of yet!')
            else:
                embed = discord.Embed()
                embed.title = f'Results for {addiction} addiction - reset'
                embed_time(embed,res)
                await ctx.send(f'{ctx.author.mention}, your {addiction} addiction has been reset')
                await ctx.send(embed = embed)
        elif not len(addiction):
            #react to remove_addiction specific addiction
            embed = discord.Embed()
            embed.title = "ALL OF THEM reset"
            #embed_emoji
            await ctx.send(embed=embed)
        else:
            await ctx.send(f'{ctx.author.mention}, could not find {addiction} addiction!')


    def embed_all_addiction(self,embed):
        for i in valid_addictions:
            addiction = i
            number_of_users_addicted = adic.count_users_addicted(addiction)
            format_addiction = addiction[0].upper()+addiction[1:]
            embed.add_field(name = format_addiction, value = f'{number_of_users_addicted} people', inline=True)
        return embed

    def embed_emoji_to_addiction(self,embed):
        pass

def setup(bot):
    bot.add_cog(addictions(bot))