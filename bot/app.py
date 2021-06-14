import discord
from discord.ext import commands
import urllib.parse, urllib.request, re
import configparser

client = commands.Bot(command_prefix="!")
client.remove_command('help')
config = configparser.ConfigParser()
config.read('keys.ini')

@client.event
async def on_ready():
    """Indicates that the bot has logged into Discord."""
    print('You have logged in as {0.user}'.format(client))


@client.command()
async def ping(ctx):
    """Bot replies with Pong!"""
    await ctx.send('Pong!')


@client.command()
async def mul(ctx, num1: int, num2: int):
    """Multiplies two given numbers."""
    await ctx.send(num1*num2)


@client.command()
async def youtube(ctx, *, search):
    """Takes user input and displays the first youtube video based on the input."""
    query_string = urllib.parse.urlencode({
        'search_query': search
    })
    htm_content = urllib.request.urlopen(
       f'http://www.youtube.com/results?search_query={query_string}'
    )

    search_results = re.findall(r"watch\?v=(\S{11})", htm_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])
    # displays one search result


@client.command()
async def youtubechan(ctx, *, search):
    """Takes a user input and displays the first youtube channel based on the input DOES NOT WORK."""
    query_string = urllib.parse.urlencode({
        'search_query': search
    })
    htm_content = urllib.request.urlopen(
        f'http://www.youtube.com/results?search_query={query_string}'
    )

    search_results = re.findall(r"https://www.youtube.com/user/(\S{11})", htm_content.read().decode())
    await ctx.send(f'https://www.youtube.com/results?search_query={search_results[0]}&sp=EgIQAg%253D%253D')
    # displays one search result


@client.command(pass_context=True)
async def help(ctx):
    """Custom help command that displays a list of bot commands and what the command does."""
    embed = discord.Embed(
        colour=discord.Colour.blue()
    )

    embed.set_author(name='Help:')
    embed.add_field(name='!ping', value='Returns Pong!', inline=False)
    embed.add_field(name='!hellopablo', value='Pablo quacks at you.', inline=False)
    embed.add_field(name='!mul', value='Multiplies two given integers. I.e. !mul 2 2 displays 4.', inline=False)
    embed.add_field(name='!youtube', value='Displays a youtube video. I.e. !youtube never gonna give you up displays '
    'http://www.youtube.com/watch?v=dQw4w9WgXcQ.', inline=False)


    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

# Make sure you don't have a command called "commands"
@client.command() # As usual
@commands.has_permissions(administrator=True) # Making sure the person executing the command has the permissions
async def foo(ctx):
	await ctx.send("Hello")
    #ect


@client.command()
async def hellopablo(ctx):
    """The bot replies to the user and displays their name."""
    author = ctx.message.author
    await ctx.send(f'Quack quack {author}!')

client.run(f'{config["KEY"]["key"]}')


