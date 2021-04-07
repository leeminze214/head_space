import discord
from discord.ext import commands
from datetime import datetime
from apis.user import user
from apis.adic import adic
from custom.decors import is_user
from custom.funcs import embed_time,string_time
from custom.refers import valid_addictions, time_names



class addictions(commands.Cog):


    @commands.command(aliases=['leaders','leaderboard','leader','leaderboards'])
    async def leader_boards(self,ctx,addiction):
        '''
            fetch top 15 users who have been sober from <addiction> for longest time
        '''
        res = adic.leader_boards(ctx,addiction)

        await ctx.send(res)

    

    @commands.command(aliases=['all'])
    async def list_all_addictions(self,ctx):       
        embed = discord.Embed()
        embed.title = "Addictions"  
        addictions_embeded = self.embed_all_addiction(embed)
        await ctx.send(embed = addictions_embeded)


    @commands.command(aliases=['pr','record','records'])
    @is_user
    async def personal_records(self,ctx,addiction=''):
        '''
            fetch top 5 records
            if no addiction given, getch top record from each addiction
        '''
        pass

    @commands.command(aliases=['list'])
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



    @commands.command(aliases=['add'])
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




    @commands.command(aliases=['remove'])
    @is_user
    async def remove_addiction(self,ctx,addiction =''):
        await self.update_addiction(ctx,addiction,'removed')



    @commands.command(aliases=['reset'])
    @is_user
    async def reset_addictions(self,ctx, addiction =""):
        await self.update_addiction(ctx,addiction,'reset')


    @commands.command()
    async def test(self,ctx):
        a = adic.leader_boards('gaming')
        await ctx.send(a)

    

    async def update_addiction(self,ctx,addiction,action):
        addiction = addiction.lower()
        if addiction in valid_addictions:
            res = adic.update_addiction(ctx.author.id,addiction,action=action)
            
            #res is dt.timedelta object xdays,h:m:s:f
            if not res:
                await ctx.send(f'{ctx.author.mention}, {addiction} is not being keep track of yet!')
            else:
                data = adic.convert_dt_to_list(res)
                personal_best = adic.personal_best(ctx.author.id,addiction,res)
                embed = discord.Embed()
                if personal_best:
                    embed.title = f'Results for {addiction} addiction - Personal Best!'
                else:
                    embed.title = f'Results for {addiction} addiction'
                embed_time(embed,data)
                await ctx.send(f'{ctx.author.mention}, your {addiction} addiction has been {action}!')
                await ctx.send(embed = embed)
        elif not len(addiction):
            #react to update_addiction a specific addiction
            embed = discord.Embed()
            embed.title = f"ALL OF THEM {action}"
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