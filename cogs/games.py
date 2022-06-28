import discord
from discord.ext import commands
import random
import time
import asyncio


class games(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()  # Rock Paper Scissors
        @commands.cooldown(1, 3, commands.BucketType.user)
        async def rps(ctx, *, decision=None):
            weapons = ["rock", "paper", "scissors"]
            choice = random.choice(weapons)
            decision = decision.lower()

            if decision not in weapons:
                return await ctx.send("Please enter a valid choice")

            if decision == choice:
                return await ctx.send(f"I choose {choice}. It's a Tie!")

            def win(decision, choice):
                if (decision == 'rock' and choice == 'scissors')or (decision == 'scissors' and choice == 'paper') or (decision == 'paper' and choice == 'rock'):
                    return True

            if win(decision, choice):
                return await ctx.send(f"I choose {choice}. You Win!")
            return await ctx.send(f"I choose {choice}. You Lose!")



        @client.command(aliases=["bowling", "roll"])  # bowling
        @commands.cooldown(1, 3, commands.BucketType.user)
        async def bowl(ctx):
            outcomes = ["You've YEETED the ball out of existence!!!",
                        "Strike!!",
                        "Oohh, seems you've missed all the pins",
                        "Do you even know how to aim that thing?",
                        "Don't throw it at the children!!!",
                        "You have demolished the bowling alley, are you proud?",
                        "Strike!!",
                        "What a strike!",
                        "Close one! Only 2 pins left",
                        "I take it you don't go bowling often?",
                        "Nice Strike, You're really good at this",
                        "Only 1 pin left!",
                        "You hit 3 pins xD",
                        "Sir! The alley is this way",
                        "Nice Spare!",
                        "Strike!!",
                        "Epic fail xD",
                        "Strike! You might be the best bowler I've ever seen",
                        "You broke a finger trying to throw the ball"
                        ]

            embed = discord.Embed(description="Rolling...", color=discord.Color.orange())
            await ctx.send(embed=embed)

            time.sleep(1)

            embed = discord.Embed(description=f"{random.choice(outcomes)}", color=discord.Color.orange())
            await ctx.send(embed=embed)

        @client.command(name="coinflip", aliases=['cf', 'flip', 'headstales', 'ct', 'cointoss', 'toss'])
        @commands.cooldown(1, 3, commands.BucketType.user)
        async def coinflip(ctx, guess):
            guess = guess.lower()
            coin = ["heads", "tails"]
            outcome = random.choice(coin)

            while guess in coin:
                embed = discord.Embed(name='Heads or Tails', color=discord.Color.orange())
                embed.set_thumbnail(url=ctx.author.avatar_url)
                if str(guess) == str(outcome):
                    embed.add_field(name=f"The outcome is {outcome}",
                                    value=f"You have guessed correctly!", inline=False)
                else:
                    embed.add_field(name=f"The outcome is {outcome}",
                                    value="Better luck next time!", inline=False)
                return await ctx.send(embed=embed)
            await ctx.send("That is not a valid option")

        @client.command(name='guess', aliases=['guessnumber', 'num', 'number'])
        @commands.cooldown(1, 3, commands.BucketType.user)
        async def guess(ctx):
            cpu = random.randint(1,10)
            chances = 3

            embed=discord.Embed(description='Im thinking of a number between 1 and 10. You have 3 guesses:',
                                color=discord.Color.orange())
            await ctx.send(embed=embed)

            def check(m):
                return m.author == ctx.author

            while chances != 0:
                try:
                    guess = await client.wait_for(event='message', check=check, timeout=7.0)
                except asyncio.TimeoutError:
                    client.get_command("guess").reset_cooldown(ctx)
                    return await ctx.send("You did not respond in time. Be quicker next time!")
                else:
                    if guess.content == str(cpu):
                        embed = discord.Embed(description="Congratulations! You've guessed correctly",
                                              color=discord.Color.orange())
                        return await ctx.send(embed=embed)
                    else:
                        chances -= 1
                        await ctx.send(f"Incorrect! You have {chances} chances left")

            embed = discord.Embed(description=f"The number was {cpu}. Better luck next time",
                                  color=discord.Color.orange())
            await ctx.send(embed=embed)

        @client.command(name='fight', aliases=['duel', '1v1'])
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def fight(ctx, member: discord.Member):

            p1 = 100
            p2 = 100
            done = False

            if member == ctx.author:
                client.get_command("fight").reset_cooldown(ctx)
                return await ctx.send("You can not fight yourself!")


            embed = discord.Embed(title='Duel!',
                                  description=f'{member.mention}, {ctx.author.name} has challenged you to a fight to the death\n'
                                              f'Respond by typing either `accept` or `retreat`',
                                  color=discord.Color.orange())
            await ctx.send(embed=embed)

            def check(m):
                return m.author == member

            try:
                answer = await client.wait_for(event='message', check=check, timeout=10.0)
            except asyncio.TimeoutError:
                client.get_command("fight").reset_cooldown(ctx)
                return await ctx.send("You did not respond in time. Be quicker next time!")
            else:
                if answer.content.lower() == 'retreat':
                    embed = discord.Embed(description=f'{ctx.author.mention}! {member.name} has declined your challenge', color=discord.Color.orange())
                    return await ctx.send(embed=embed)
                elif answer.content.lower() == 'accept':
                    embed = discord.Embed(
                        description=f'Duel: {ctx.author.name} & {member.name} are fighting to the death',
                        color=discord.Color.orange())
                    embed.add_field(name=ctx.author.name, value=f"Health: {p1}", inline=True)
                    embed.add_field(name=member.name, value=f"Health: {p2}", inline=True)
                    msg = await ctx.send(embed=embed)

                    while done is False:
                        e = discord.Embed(
                            description=f'Duel: {ctx.author.name} & {member.name} are fighting to the death',
                            color=discord.Color.orange())
                        e.add_field(name=ctx.author.name, value=f"Health: {p1}", inline=True)
                        e.add_field(name=member.name, value=f"Health: {p2}", inline=True)

                        damage = random.randint(4, 17)

                        turn = random.randint(1, 2)
                        if turn == 1:
                            if p1 < 25:
                                damage = random.randint(1,3)
                            p1 = p1 - damage
                            if p1 - damage <= 0:
                                p1 = 0
                        elif turn == 2:
                            if p2 < 25:
                                damage = random.randint(1,3)
                            p2 = p2 - damage
                            if p2 - damage <= 0:
                                p2 = 0

                        time.sleep(1)
                        await msg.edit(embed=e)

                        if p1 == 0:
                            f = discord.Embed(
                                description=f'{member.mention} has defeated {ctx.author.mention} and won the fight!',
                                color=discord.Color.orange())
                            f.add_field(name=ctx.author.name, value=f"Health: 0", inline=True)
                            f.add_field(name=member.name, value=f"Health: {p2}", inline=True)
                            return await msg.edit(embed=f)
                        elif p2 == 0:
                            f = discord.Embed(
                                description=f'{ctx.author.mention} has defeated {member.mention} and won the fight!',
                                color=discord.Color.orange())
                            f.add_field(name=ctx.author.name, value=f"Health: {p1}", inline=True)
                            f.add_field(name=member.name, value=f"Health: 0", inline=True)
                            return await msg.edit(embed=f)


def setup(bot):
    bot.add_cog(games(bot))
