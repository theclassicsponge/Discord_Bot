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
    print('You have logged in as {0.user}'.format(client))


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')


@client.command()
async def mul(ctx, num1: int, num2: int):
    """Multiplies two given numbers."""
    await ctx.send(num1*num2)


@client.command()
async def youtube(ctx, *, search):
    """DOESN'T WORK"""
    query_string = urllib.parse.urlencode({
        'search_query': search
    })
    htm_content = urllib.request.urlopen(
       'http://www.youtube.com/results?' + query_string
    )

    search_results = re.findall('r="watch\?v=(\S{11})', htm_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])
    # displays one search result


@client.command(pass_context=True)
async def help(ctx):
    """Custom help command that displays a list of bot commands and what the command does."""
    embed = discord.Embed(
        colour=discord.Colour.orange()
    )

    embed.set_author(name='Help:')
    embed.add_field(name='!ping', value='Returns Pong!', inline=False)
    embed.add_field(name='!hellopablo', value='Pablo quacks at you.', inline=False)
    embed.add_field(name='!mul', value='Multiplies two given integers. I.e. !mul 2 2 displays 4.', inline=False)


    await ctx.send(embed=embed)


@client.command()
async def hellopablo(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello {author}!')

client.run(f'{config["KEY"]["key"]}')
