import discord
import random
from discord.ext import commands, tasks
from itertools import cycle
import logging
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8c32a9e (Refactor to use environment variables for API tokens and credentials)
import os
from dotenv import load_dotenv

# Discord API Token
load_dotenv()
token = os.getenv('Discord_API_Token')

# Reddit API
reddit_client_id = os.getenv('Reddit_Client_ID')
reddit_client_secret = os.getenv('Reddit_Client_Secret')
reddit_user= os.getenv('Reddit_Username')
reddit_password = os.getenv('Reddit_Password')
<<<<<<< HEAD
=======
>>>>>>> bdb96dd (Add logging functionality and update message handling for reactions)
=======
>>>>>>> 8c32a9e (Refactor to use environment variables for API tokens and credentials)

# Logging
logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO
)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
<<<<<<< HEAD

client = commands.Bot(command_prefix='/', intents=intents)

status = cycle(["Ruf Ruf", "Viu Viu", "Bark Bark", "Licking balls"])

# Reddit API cost money, so I wont use it.
""" reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent="Remu botti",
                     username=reddit_user,
                     password=reddit_password) """

=======

client = commands.Bot(command_prefix='/', intents=intents)

status = cycle(["Ruf Ruf", "Viu Viu", "Bark Bark", "Licking balls"])

# Reddit API cost money, so I wont use it.
""" reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent="Remu botti",
                     username=reddit_user,
                     password=reddit_password) """

>>>>>>> bdb96dd (Add logging functionality and update message handling for reactions)
# Emojit
BIG_THINK = "<:big_think:1274396489686323300>"
NAUTIN = "<:nautin:1195694506780151818>"
VITUN_KALJU = "<:vitun_kalju:1165679237500514355>"
KALJU_VITUN = "<:kalju_vitun:1281950244556374036>"

@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if 'bark' in message.content.lower():
            await message.channel.send("grr")
        elif 'grr' in message.content.lower():
            await message.channel.send("bark")
        elif 'uli' in message.content.lower():
            await message.channel.send("viu viu")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        elif 'remu' in message.content.lower():
            await message.channel.send("woof")
=======
=======
        elif 'kalju' in message.content.lower() and 'henry' in message.content.lower():
            await message.add_reaction(VITUN_KALJU)
            await message.add_reaction(KALJU_VITUN)
>>>>>>> 230a81b (Add reactions for combined 'kalju' and 'henry' mentions in message handler)
=======
>>>>>>> bdb96dd (Add logging functionality and update message handling for reactions)
=======
        elif 'kalju' in message.content.lower() and 'henry' in message.content.lower():
            await message.add_reaction(VITUN_KALJU)
            await message.add_reaction(KALJU_VITUN)
>>>>>>> 230a81b (Add reactions for combined 'kalju' and 'henry' mentions in message handler)
        elif 'kalju' in message.content.lower():
            await message.add_reaction(VITUN_KALJU)
        elif 'henry' in message.content.lower():
            await message.add_reaction(KALJU_VITUN)
    await client.process_commands(message)
>>>>>>> bdb96dd (Add logging functionality and update message handling for reactions)


@client.command()
async def meme(ctx):
    # submission = reddit.subreddit('memes').random()
    await ctx.send(f"Reddit API maksaa rahaa, joten en voi käyttää sitä.\nUutta ratkaisua etsitään. {NAUTIN}")


@client.command()
async def perse(ctx):
    # submission = reddit.subreddit('ass').random()
    await ctx.send(f"Reddit API maksaa rahaa, joten en voi käyttää sitä.\nUutta ratkaisua etsitään. {NAUTIN}")


@client.command()
async def tissit(ctx):
    # submission = reddit.subreddit('boobs').random()
    await ctx.send(f"Reddit API maksaa rahaa, joten en voi käyttää sitä.\nUutta ratkaisua etsitään. {NAUTIN}")


@client.command()
async def doggo(ctx):
    # submission = reddit.subreddit('rarepuppers').random()
    await ctx.send(f"Reddit API maksaa rahaa, joten en voi käyttää sitä.\nUutta ratkaisua etsitään. {NAUTIN}")


@client.command()
async def catto(ctx):
    # submission = reddit.subreddit('lolcats').random()
    await ctx.send(f"Reddit API maksaa rahaa, joten en voi käyttää sitä.\nUutta ratkaisua etsitään. {NAUTIN}")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Anna kaikki argumentit pls ;_;")


<<<<<<< HEAD
<<<<<<< HEAD
@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    ctx.send("Loaded cogs")


@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    ctx.send("Unloaded cogs")
=======
=======
>>>>>>> bdb96dd (Add logging functionality and update message handling for reactions)
# Mitä vittua nämä edes ovat?
# @client.command()
# @commands.has_permissions(administrator=True)
# async def load(ctx, extension):
#     client.load_extension(f"cogs.{extension}")
#     ctx.send("Loaded cogs")
#
#
# @client.command()
# @commands.has_permissions(administrator=True)
# async def unload(ctx, extension):
#     client.unload_extension(f"cogs.{extension}")
#     ctx.send("Unloaded cogs")
>>>>>>> bdb96dd (Add logging functionality and update message handling for reactions)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    change_status.start()
    logging.info("Remu-botti is operational.")


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} potkittu ulos")


@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} Bänned")


@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.name}#{user.discriminator}")
            return


@client.command()
async def remuh(ctx, *, question):
    responses = ["Se on varma.",
                 "Se on ehdottomasti niin.",
                 "Epäilemättä.",
                 "Kyllä ehdottomasti.",
                 "Voit luottaa siihen.",
                 "Kuten näen, kyllä.",
                 "Todennäköisimmin.",
                 "Tulevaisuudennäkymä hyvä.",
                 "Joo.",
                 "Merkit osoittavat kyllä.",
                 "Älä luota siihen.",
                 "Vastaukseni on ei.",
                 "Lähteeni sanovat ei.",
                 "Näkymät eivät ole niin hyvät.",
                 "Hyvin epätodennäköistä.",
                 "dunno lelol <:big_think:1274396489686323300>"]
    if 'kalju' in question.lower():
        await ctx.send(f"{VITUN_KALJU}")
    else:
        await ctx.send(f"Kysymys: {question}\nVastaus: {random.choice(responses)}")


@tasks.loop(minutes=2)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(token)
