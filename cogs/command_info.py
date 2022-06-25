import discord
from discord.ext import commands


class commandsInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["help"])  # commands/help
    async def commands(self, ctx, *, category=None):
        if category is None:
            embed = discord.Embed(
                title="A list of all my current commands/features",
                description="Descriptions are provided below each command\n" 
                            "[Support Server](https://discord.gg/fa3j7fpbA6/ 'Takes you to the official KoffeeBot "
                            "discord')",
                color=discord.Color.orange()
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')
            embed.add_field(name=":tada: kof help fun", value="Displays all fun related commands",inline=True)
            embed.add_field(name=":moneybag: kof help economy", value="Displays all economy commands", inline=True)
            embed.add_field(name=":game_die: kof help games", value="Displays all game related commands",inline=True)
            embed.add_field(name=":shield: kof help moderation", value="Displays all moderation commands",inline=True)
            embed.add_field(name=":jigsaw: kof help images", value="Displays all image manipulation commands",inline=True)
            embed.add_field(name=":pushpin: kof help misc", value="Displays all miscellaneous commands ", inline=True)
            embed.add_field(name="<:hat:984285090190360657> kof help mafia", value="Displays all mafia commands ", inline=True)

            await ctx.send(embed=embed)
            return

        if category.lower() == "moderation":
            embed = discord.Embed(
                title="Moderation",
                description="Descriptions are provided below each command\n"
                            "[Support Server](https://discord.gg/fa3j7fpbA6/ 'Takes you to the official KoffeeBot "
                            "discord')",
                color=discord.Color.orange())
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')
            embed.add_field(name=":wastebasket: kof clear [Amount]", value="Deletes a specified amount of text messages", inline=True)
            embed.add_field(name=":mute: kof mute [user] [Reason]", value="Mutes someone", inline=True)
            embed.add_field(name=":sound: kof unmute [user]", value="Unmutes someone\n", inline=True)
            embed.add_field(name=":foot: kof kick [user] [Reason]", value="Kicks someone from the server", inline=True)
            embed.add_field(name=":hammer: kof ban [user] [Reason]", value="Bans someone from the server",
                            inline=True)
            embed.add_field(name=":tools: kof unban [user]", value="Unbans someone\n", inline=True)
            embed.add_field(name=":tickets: kof giverole [role] [user]", value="Give someone a role from your server",
                            inline=True)
            embed.add_field(name=":carpentry_saw: kof removerole [role] [user]", value="Remove a role from someone",
                            inline=True)
            await ctx.send(embed=embed)

        elif category.lower() == "misc":
            embed = discord.Embed(
                title="Miscellaneous",
                description="Descriptions are provided below each command\n"
                            "[Support Server](https://discord.gg/fa3j7fpbA6/ 'Takes you to the official KoffeeBot "
                            "discord')",
                color=discord.Color.orange()
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')
            embed.add_field(name=":wave: kof greet", value="KoffeeBot introduces\n itself", inline=True)
            embed.add_field(name=":thumbsup: kof poll [message]", value="Creates a poll", inline=True)
            embed.add_field(name=":sewing_needle: kof nick [user] [nickname]", value="Change the nickname of a specified user",
                            inline=True)
            embed.add_field(name=":performing_arts: kof avatar", value="View a user's profile picture", inline=True)
            embed.add_field(name=":bellhop: kof invite", value="Add KoffeeBot to other servers", inline=True)
            embed.add_field(name=':hourglass: kof support', value="Have any problems with KoffeeBot?")
            embed.add_field(name=':chart_with_upwards_trend: kof servers', value="Check how many servers are using KoffeeBot")
            await ctx.send(embed=embed)

        elif category.lower() == "fun":
            embed = discord.Embed(
                title="Fun",
                description="Descriptions are provided below each command\n"
                            "[Support Server](https://discord.gg/fa3j7fpbA6/ 'Takes you to the official KoffeeBot "
                            "discord')",
                color=discord.Color.orange()
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')
            embed.add_field(name=":8ball: kof 8ball [Question]", value="Ask the magical 8ball any question you like",
                            inline=True)
            embed.add_field(name=":rofl: kof roast", value="Roasts someone", inline=True)
            embed.add_field(name=":eyes: kof simp", value="Are you a simp?\n", inline=True)
            embed.add_field(name=":brain: kof dumb", value="Checks how stupid someone is", inline=True)
            embed.add_field(name=":rainbow_flag: kof gay", value="How gay are you really?\n", inline=True)
            embed.add_field(name=":smile: kof laugh", value="KoffeeBot will awkwardly laugh", inline=True)
            embed.add_field(name=":roll_of_paper: kof meme", value="Enjoy some quality memes!", inline=True)
            embed.add_field(name="⭕ kof o [message]", value="Replace all vowels with the letter 'o'", inline=True)
            embed.add_field(name=":sparkles: kof insult", value="Curse someone with the mildest of inconveniences",
                            inline=True)
            await ctx.send(embed=embed)

        elif category.lower() == "games":
            embed = discord.Embed(
                title="Games",
                description="Descriptions are provided below each command\n"
                            "[Support Server](https://discord.gg/fa3j7fpbA6/ 'Takes you to the official KoffeeBot "
                            "discord')",
                color=discord.Color.orange()
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')
            embed.add_field(name=":scissors: kof rps [choice]", value="Play a game of Rock, Paper, Scissors", inline=True)
            embed.add_field(name=":regional_indicator_x: kof tictactoe [Player 1] [Player 2]", value="Who doesn't "
                                                                                                     "love\ntic tac "
                                                                                                     "toe", inline=True)
            embed.add_field(name=":bowling: kof bowl", value="Enjoy some bowling\n", inline=True)
            embed.add_field(name="⭕ kof coinflip [choice]", value="Heads or Tails!!!",inline=True)
            embed.add_field(name="❓ kof guess", value="Guess the number game!", inline=True)
            await ctx.send(embed=embed)

        elif category.lower() == "economy":  # economy
            embed = discord.Embed(
                title="Economy",
                description="Descriptions are provided below each command\n"
                            "[Support Server](https://discord.gg/fa3j7fpbA6/ 'Takes you to the official KoffeeBot "
                            "discord')",
                color=discord.Color.orange()
            )
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')
            embed.add_field(name="💳 kof bal", value="Check your balance/ open an account")
            embed.add_field(name='💼 kof inv', value="Displays your inventory")
            embed.add_field(name=':calendar: kof daily', value="Receive your daily amount of <:KoffeeKoin:939562780363726868>")
            embed.add_field(name=':screwdriver: kof work', value="Start working for some <:KoffeeKoin:939562780363726868>")
            embed.add_field(name='⏰ kof jobs', value="You might need a job to earn <:KoffeeKoin:939562780363726868>")
            embed.add_field(name='🗄️ kof resign', value="Quit your current job")
            embed.add_field(name='🙏 kof beg', value="Beg for people to give you <:KoffeeKoin:939562780363726868>")
            embed.add_field(name='🍀 kof lucky', value="Do you think you're lucky?")
            embed.add_field(name=":diamonds: kof scam", value="So now you're taking people's money?")
            embed.add_field(name='💼 kof withdraw [amount]', value="Withdraw money from the bank")
            embed.add_field(name='💸 kof give [user] [amount] [item]', value="Give the poor people their money")
            embed.add_field(name='🏛️ kof dep [amount]', value="Deposit <:KoffeeKoin:939562780363726868> into your bank account.")
            embed.add_field(name='🛒 kof shop', value="Opens up the KoffeeBot shop")
            embed.add_field(name='🛍️ kof buy [item] [amount]', value="Buy an item from the shop")
            embed.add_field(name='💰 kof sell [item] [amount]', value="Sell an item from your inventory")
            embed.add_field(name=':smiling_imp: kof steal [user]', value="Attemp to steal <:KoffeeKoin:939562780363726868> from someone")
            embed.add_field(name='🍽️ kof recipes', value="Shows all craftable items")
            embed.add_field(name='⛏ kof craft [item] [amount]', value="Craft an item")
            embed.add_field(name=':slot_machine: kof slots [amount]', value="Risk it all with the slot machine!")
            embed.add_field(name='💎 kof rich', value="View the richest KoffeeBot users in your discord")

            await ctx.send(embed=embed)

        elif category.lower() == "images":  # Images
            embed = discord.Embed(
                title="Image Manipulation",
                description="Descriptions are provided below each command\n"
                            "[Support Server](https://discord.gg/fa3j7fpbA6/ 'Takes you to the official KoffeeBot "
                            "discord')",
                color=discord.Color.orange()
            )
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')
            embed.add_field(name=":detective: kof wanted", value="Shows your wanted picture", inline=True)
            embed.add_field(name=":coffin: kof rip", value="You died?", inline=True)
            embed.add_field(name=":punch: kof hit [user]", value="Punch someone!\n", inline=True)
            embed.add_field(name=":dancer: kof dance", value="Enjoy some cool dance moves!", inline=True)
            embed.add_field(name=":clap: kof slap [user]", value="Slap someone!", inline=True)
            embed.add_field(name=":hugging: kof hug [user]", value="Hug someone", inline=True)
            embed.add_field(name=":broken_heart: kof ship [user]", value="See you chances of shipping with someone",
                            inline=True)
            embed.add_field(name=":japanese_ogre: kof evil", value="Are you really that evil?", inline=True)
            embed.add_field(name=":gun: kof shoot [user]", value="Shoot someone", inline=True)
            embed.add_field(name=":rage: kof angry", value="Let all that rage out", inline=True)
            embed.add_field(name=":eyes: kof threaten [user]", value="Make sure this person stays quiet",
                            inline=True)
            await ctx.send(embed=embed)

        elif category.lower() == "mafia":
            embed = discord.Embed(
                title="Mafia",
                description="Descriptions are provided below each command\n"
                            "[Support Server](https://discord.gg/fa3j7fpbA6/ 'Takes you to the official KoffeeBot "
                            "discord')",
                color=discord.Color.orange()
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')
            embed.add_field(name="<:hat:984285090190360657> kof mafia", value="Displays your mafia profile", inline=True)
            embed.add_field(name="🚬 kof mafia create [name]", value="Create a mafia", inline=True)
            embed.add_field(name="✉ kof mafia invite [user]", value="Invite someone into your mafia", inline=True)
            embed.add_field(name="👌 kof promote [user]", value="Promote someone in your mafia", inline=True)
            embed.add_field(name="🦴 kof demote [user]", value="Demote someone in your mafia", inline=True)
            embed.add_field(name="👞 kof mafia kick [target]", value="Kick someone from your mafia", inline=True)
            embed.add_field(name="💼 kof mafia leave", value="Leave your current mafia", inline=True)
            embed.add_field(name="🧨 kof mafia delete", value="Delete a mafia you have created", inline=True)
            embed.add_field(name="🧱 kof heist [target]", value="Attemp to rob someone's bank account", inline=True)
            embed.add_field(name="🔑 kof vault withdraw [amount]", value="Withdraw <:KoffeeKoin:939562780363726868> from your vault", inline=True)
            embed.add_field(name="🗝️ kof vault deposit [amount]", value="Deposit <:KoffeeKoin:939562780363726868> into your vault", inline=True)
            await ctx.send(embed=embed)

        else:
            await ctx.send("Please enter a valid category")


def setup(bot):
    bot.add_cog(commandsInfo(bot))
