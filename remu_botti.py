import discord
import random
import os
import praw
from discord.ext import commands, tasks
from itertools import cycle

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)
status = cycle(["Ruf Ruf", "Viu Viu", "Bark Bark", "Licking balls"])
reddit = praw.Reddit(client_id="qktlYkc_B9XuBA",
                     client_secret="6HBKxc1Hz61n4EYsEFn18K7MXQo",
                     user_agent="Remu botti",
                     username="Z8zeR",
                     password="Subaru129")


@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if 'bark' in message.content.lower():
            await message.channel.send("grr")
        elif 'grr' in message.content.lower():
            await message.channel.send("bark")
        elif 'uli' in message.content.lower():
            await message.channel.send("viu viu")
        elif 'remu' in message.content.lower():
            await message.channel.send("woof")
    await client.process_commands(message)


@client.command()
async def meme(ctx):
    submission = reddit.subreddit('memes').random()
    await ctx.send(submission.title)
    await ctx.send(submission.url)


@client.command()
async def perse(ctx):
    submission = reddit.subreddit('ass').random()
    await ctx.send(submission.url)


@client.command()
async def tissit(ctx):
    submission = reddit.subreddit('boobs').random()
    await ctx.send(submission.url)


@client.command()
async def doggo(ctx):
    submission = reddit.subreddit('rarepuppers').random()
    await ctx.send(submission.url)


@client.command()
async def catto(ctx):
    submission = reddit.subreddit('lolcats').random()
    await ctx.send(submission.url)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Anna kaikki argumentit pls ;_;")


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


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    change_status.start()
    print("Remu-botti is operational.")


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
                 "dunno lelol"]
    await ctx.send(f"Kysymys: {question}\nVastaus: {random.choice(responses)}")


@tasks.loop(minutes=2)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


# for filename in os.listdir('./cogs'):
#     if filename.endswith('.py'):
#         client.load_extension(f"cogs.{filename[:-3]}")

client.run('NzU2MTE4MDIyMjM3OTc4NzE1.X2NLyA.GBlNY4eNk1YVH6ewveutr-zfny4')
