import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import random


class utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command(aliases=["hey", "hi"])  # Hello command
        async def greet(ctx):
            hey = ["Hello there!", "Helloo", "Hey!", "Yo!", "Wazzup", f"Greetings {ctx.author.name}!", "Sup",
                   f"Hi {ctx.author.name}"]
            if ctx.message.author.id == 465839240777826324:  # Me
                await ctx.message.channel.send('Good to see you master')
                return
            elif ctx.message.author.id == 660749269921169410:  # sheepy
                await ctx.message.channel.send('Hello Sheep')
                return
            elif ctx.message.author.id == 316436801499693066:  # Diorice
                await ctx.message.channel.send('Good day mr Diorice sir!')
                return
            elif ctx.message.author.id == 324570286068334592:  # janlu
                await ctx.message.channel.send('My lord!')
                return
            elif ctx.message.author.id == 327888112808099840:  # vir gerhard van janlu
                await ctx.message.channel.send('jys kak in war tunder, van janlu #gethacked')
                return
            elif ctx.message.author.id == 190877518029520896:  # vir juan van janlu
                await ctx.message.channel.send('jys kak in leugue og legends #getgoodfam')
                return
            await ctx.send(random.choice(hey))


        @client.command()  # make a poll
        async def poll(ctx, question, *options: str):
            if len(options) <= 1:
                await ctx.send('You need more than one option to make a poll!')
                return
            if len(options) > 10:
                await ctx.send('You cannot make a poll for more than 10 things!')
                return

            if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
                reactions = ['✅', '❌']
            else:
                reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

            description = []
            for x, option in enumerate(options):
                description += '\n {} {}'.format(reactions[x], option)
            embed = discord.Embed(title=question, description=''.join(description), color=discord.Color.orange())
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')
            embed.set_footer(text=f"Poll created by {ctx.author}", icon_url=ctx.author.avatar_url)
            react_message = await ctx.send(embed=embed)
            for reaction in reactions[:len(options)]:
                await react_message.add_reaction(reaction)
            await react_message.edit_message(embed=embed)

        @client.command(pass_context=True)  # change nickname
        @has_permissions(manage_nicknames=True)
        async def nick(ctx, member: discord.Member, nickname):
            await member.edit(nick=nickname)
            await ctx.send(f'Changed nickname to {nickname} ')

        @client.command(aliases=["av"])  # avatar command
        async def avatar(ctx, *, target: discord.Member = None):
            if target is None:
                target = ctx.author
                em = discord.Embed(title="Avatar", color=discord.Color.orange())
                em.set_author(name=target, icon_url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')
                em.set_image(url=target.avatar_url)
                await ctx.send(embed=em)
            else:
                em = discord.Embed(title="Avatar", color=discord.Color.orange())
                em.set_author(name=str(target),
                              icon_url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')
                em.set_image(url=target.avatar_url)
                await ctx.send(embed=em)

        @client.command(aliases=["sup"])  # support discord server
        async def support(ctx):
            embed = discord.Embed(color=discord.Color.orange())
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')
            embed.add_field(name='KoffeeBot support', value="Have any problems with KoffeeBot? Tell us here!\n[Support "
                                                            "Server](https://discord.gg/fa3j7fpbA6/ "
                                                            "'Takes you to the official KoffeeBot discord')")
            await ctx.send(embed=embed)

        @client.command(aliases=['link'])  # Invite bot link
        async def invite(ctx):
            embed = discord.Embed(
                color=discord.Color.orange()
            )
            embed.add_field(name="Add me to other servers :D",
                            value="https://top.gg/bot/901223515242508309?s=0210af7e1c4e5",
                            inline=False)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(utilities(bot))
