import discord
from discord.ext import commands, tasks
from discord.ext.commands import MissingPermissions, MissingRequiredArgument
import random
import time
import os
from os import environ
from dotenv import load_dotenv
from itertools import cycle
from discord.utils import find

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix=['kof ', 'Kof '], intents=intents, case_insensitive=True)
client.remove_command('help')
status = cycle(["kof help",
                "with your feelings",
                "Phasmophobia 4",
                "Dead by nightlight",
                "Rainbow Seven Siege",
                "Fortnite 2",
                "War Lightning",
                "Genshin Impact 2.0",
                "Destiny 3",
                "Little Foot",
                "League of Legends 2",
                "The Sims 5",
                "Far Cry 9",
                "Brawlhalla 2",
                "Overwatch 3",
                "Among You",
                "Minecraft 2",
                "Rocket League 2",
                "Rust 4",
                "Borderlands 5",
                "The Witcher 6",
                "GTA VII",
                "Elden Ring 3",
                "Cyberpunk 420",
                "COD BO 5"])  # Bot status games


# tictactoe variables
player1 = ""
player2 = ""
turn = ""
gameOver = True
board = []
winningconditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


@client.event  # Bot is ready
async def on_ready():
    change_status.start()
    print('Online as {0.user}'.format(client))
    print(f"Currently in {len(client.guilds)} servers")


   # discord_guild = client.guilds[-1]
   # print(discord_guild)
   # invite = await discord_guild.text_channels[0].create_invite(max_uses=1)
   # print(invite)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


@client.event  # on guild join
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send("Hi, I'm KofeeBot. Use **kof help** to get started!")


@client.event  # error events
async def on_command_error(ctx, error):
    if isinstance(error, MissingPermissions): # missing permissions
        embed = discord.Embed(color=discord.Color.orange())
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')
        embed.add_field(name="Missing Permissions", value="You don't have the required\npermissions to do that!")
        msg = await ctx.send(embed=embed)
        time.sleep(5)
        await msg.delete()

    elif isinstance(error, MissingRequiredArgument): # missing an argument in command
        embed = discord.Embed(color=discord.Color.orange())
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')
        embed.add_field(name="Missing an Argument", value="Not all the requirements have been met.\nMake sure you are "
                                                          "using the command correctly\n Use **kof help** to help "
                                                          "with using a command")
        msg = await ctx.send(embed=embed)
        time.sleep(5)
        await msg.delete()
        client.get_command(ctx.invoked_with).reset_cooldown(ctx)

    elif isinstance(error, commands.CommandOnCooldown): # cooldown handling

        timer = error.retry_after

        if timer >= 3600:
            timer_format = "hours"
            timer = error.retry_after/3600
        elif timer >= 60:
            timer_format = "min"
            timer = error.retry_after/60
        else:
            timer_format = "seconds"

        embed = discord.Embed(color=discord.Color.orange())
        embed.set_thumbnail(
            url=ctx.author.avatar_url)
        embed.add_field(name="Cooldown", value=f"You are on cooldown!\nTry again in `{round(timer)} {timer_format}`")
        msg = await ctx.send(embed=embed)
        time.sleep(5)
        await msg.delete()


@tasks.loop(minutes=120)  # loops different status
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command(name='servers', aliases=['server'])
async def servers(ctx, arg=None):
    owner_id = 465839240777826324
    user = client.get_user(465839240777826324)
    message = ""

    if arg == "list":
        if owner_id != 465839240777826324:
            return
        for guild in client.guilds:
            message += f"{guild.name}\n"
        await user.send(message)

    embed = discord.Embed(title="KoffeeBot Server count", color=discord.Color.orange())
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/922598156842172508/923140639556775946/koffee4.png')
    embed.add_field(name=f"Currently in {len(client.guilds)} servers", value="Add me to more :D\n"
                         "https://top.gg/bot/901223515242508309?s=0210af7e1c4e5")
    await ctx.send(embed=embed)


@client.command()  # tic tac toe
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):

    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")


@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkwinner(winningconditions, mark)
                print(count)
                if gameOver is True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkwinner(winning_conditions, mark):
    global gameOver
    for condition in winning_conditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

load_dotenv()
token = environ["TOKEN"]

client.run(token)
