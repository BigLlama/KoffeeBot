import discord
from discord.ext import commands
import random
import praw
import re


class fun(commands.Cog):
    def __init__(self, client):
        self.bot = client

        @client.command()
        async def meme(ctx):
            await ctx.send("Your meme is on its way!")
            reddit = praw.Reddit(client_id='WPQU7NjhT4M9zTKCVxoRzQ',
                                 client_secret='jSKwzWRALcXyWtZ_e6ZiNGfO-Kvg5A',
                                 user_agent='pythonprawmeme')

            meme_submissions = reddit.subreddit('memes').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in meme_submissions if not x.stickied)
            await ctx.send(submission.url)

        @client.command()  # Roast (Add more roasts in future)
        async def roast(ctx, person: discord.Member = None):
            roasts = ["You are so ugly you made a happy meal cry",
                      "I'll never forget the first time I met you, but i will keep on trying",
                      "Don't be ashamed of who you are. That's your parents' job",
                      "You are like a cloud. Once you disappear, it's a lovely day",
                      "You were born on the highway, next to all the other accidents",
                      "You have your whole life to be a jerk, why not take a day off?",
                      "It's funny to think that out of all the choices you could have made, "
                      "you decided to wake up for another day",
                      "If I throw a stick, will you leave?",
                      "I thought of you today. It reminded me to take out the trash",
                      "You are the reason why shampoo bottles have instructions",
                      "Mirrors can't talk back. Luckily they can't laugh either"]

            embed = discord.Embed(
                title="Roast-inator",
                color=discord.Color.orange())
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')

            if person is not None:
                embed.add_field(name=f"{person}", value=random.choice(roasts) + " :joy:", inline=False)
            elif person is None:
                embed.add_field(name=f"{ctx.author}", value=random.choice(roasts) + " :joy:", inline=False)
            await ctx.send(embed=embed)

        @client.command(aliases=['bother', 'trouble'])
        async def insult(ctx, user: discord.Member = None):
            troubles = ["I hope there's hole in your sock perfectly fitting for your big toe to slide through",
                        "I hope your phone charger only works at a specific angle",
                        "I hope someone eats your food that you've stored in the fridge",
                        "I hope you can't find your keys when you're in a rush",
                        "I hope you get stung by a bee",
                        "I hope you step on a lego",
                        "I hope you can't find the light switch at night",
                        "I hope your pillow case keeps sliding off",
                        "I hope your favourite snack is always out of stock at the store",
                        "I hope you're never able to close the door on the first try",
                        "I hope your earphones are always tangled when you are about to use them",
                        "I hope the next time someone leaves your room they leave the door open",
                        "I hope you get 3 ads on Youtube before getting to watch your video",
                        "I hope the next time you watch a video it keeps buffering every 5 seconds",
                        "I hope the next time you wake up your phone didn't charge overnight",
                        "I hope that you insert a USB wrong at least twice before getting it right"]
            if user is None:
                user = ctx.author

            embed = discord.Embed(
                title="Mild inconveniences", color=discord.Color.orange())
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')
            embed.add_field(name=f"{user.name}", value=random.choice(troubles) + " :sparkles:", inline=False)
            await ctx.send(embed=embed)

        @client.command(aliases=["8ball", "8b"])  # 8ball
        async def _8ball(ctx, *, question=None):
            responses = ["It is certain.",
                         "It is decidedly so.",
                         "Without a doubt.",
                         "Yes definitely.",
                         "You may rely on it.",
                         " As I see it, yes.",
                         "Most likely.",
                         "Outlook good.",
                         "Yes.",
                         "Signs point to yes.",
                         "Reply hazy, try again.",
                         "Ask again later.",
                         "Better not tell you now.",
                         "Cannot predict now.",
                         "Concentrate and ask again.",
                         "Don't count on it.",
                         "My reply is no.",
                         "My sources say no.",
                         "Outlook not so good.",
                         "Very doubtful."]

            embed = discord.Embed(
                title="Magic 8-ball",
                color=discord.Color.orange())
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')

            if question is None:
                await ctx.send("Please ask a question next time!")
                return
            else:
                embed.add_field(name=f":8ball: Question: {question}", value=f":8ball: Answer: {random.choice(responses)}")
            await ctx.send(embed=embed)

        @client.command()  # gay probability
        async def gay(ctx, *, person: discord.Member = None):
            embed = discord.Embed(
                title="Gay rater",
                color=discord.Color.orange())
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')

            if person is None:
                embed.add_field(name=f"{ctx.author}", value="You are " + str(random.choices(range(1, 101))) + "% gay! :gay_pride_flag:")
            else:
                embed.add_field(name=f"{person}", value="You are " + str(random.choices(range(1, 101))) + "% gay! :gay_pride_flag:")
            await ctx.send(embed=embed)

        @client.command()  # simp probability
        async def simp(ctx, *, person: discord.Member = None):
            embed = discord.Embed(
                title="Simp machine",
                color=discord.Color.orange())
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')

            if person is None:
                embed.add_field(name=f"{ctx.author}", value="You are " + str(random.choices(range(1, 101))) + "% simp!")
            else:
                embed.add_field(name=f"{person}", value="You are " + str(random.choices(range(1, 101))) + "% simp!")
            await ctx.send(embed=embed)

        @client.command(aliases=["stupid", "iq"])  # Stupid probability
        async def dumb(ctx, *, person: discord.Member = None):
            embed = discord.Embed(
                title="Dumb calculator",
                color=discord.Color.orange())
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')

            if person is None:
                embed.add_field(name=f"{ctx.author}", value="You are " + str(random.choices(range(1, 101))) + "% "
                                                                                                              "stupid!")
            else:
                embed.add_field(name=f"{person}", value="You are " + str(random.choices(range(1, 101))) + "% stupid!")
            await ctx.send(embed=embed)

        @client.command(aliases=["haha"])  # laugh command
        async def laugh(ctx):
            laughs = ['haha', 'lol', 'haha lol', "Why? I don't see anything funny", 'lmao', 'no', "Nothing's funny "
                                                                                                  "except your face..."]
            await ctx.send(random.choice(laughs))

        @client.command()
        async def o(ctx, *, msg):
            msg = msg.lower()
            x = ''
            vowels = ['a', 'e', 'i', 'u']

            for i in range(len(vowels)):
                x = re.sub(vowels[i], 'o', msg)
                msg = x

            embed = discord.Embed(title=x, color=discord.Color.orange())
            embed.set_footer(text="inspired by Chorry")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(fun(bot))
