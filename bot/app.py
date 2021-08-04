import discord
import os
from discord.ext import commands
import urllib.parse, urllib.request, re
import configparser
import asyncpg

DEFAULT_PREFIX = "!"


async def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned(DEFAULT_PREFIX)(bot,message)

    prefix = await bot.db.fetch('SELECT prefix FROM guilds WHERE guild_id = $1', message.guild.id)
    if len(prefix) == 0:
        await bot.db.execute('INSERT INTO guilds(guild_id, prefix) VALUES ($1, $2)', message.guild.id, DEFAULT_PREFIX)
        prefix = DEFAULT_PREFIX
    else:
        prefix = prefix[0].get("prefix")
    return commands.when_mentioned_or(prefix)(bot,message)


client = commands.Bot(command_prefix= get_prefix)
client.remove_command('help')
config = configparser.ConfigParser()
config.read('keys.ini')

async def create_db_pool():
    client.db = await asyncpg.create_pool(database = "pablodb", user = "postgres", password= f'{config["PASSWORD"]["password"]}')
    print("connection successful!")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'commands.{extension}')
    await ctx.send(f'{extension} has been loaded!')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'commands.{extension}')
    await ctx.send(f'{extension} has been unloaded!')


@client.event
async def on_ready():
    """Indicates that the bot has logged into Discord."""
    print('You have logged in as {0.user}'.format(client))


@client.command()
async def ping(ctx):
    """Bot replies with Pong!"""
    await ctx.send('Pong!')


@client.command(alies=['setpre'])
@commands.has_permissions(administrator=True)
async def setprefix(ctx, new_prefix):
    await client.db.execute('UPDATE guilds SET PREFIX = $1 where guild_id = $2', new_prefix, ctx.guild.id)
    await ctx.send("Prefix Updated!")
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
# 123



for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')

client.loop.run_until_complete(create_db_pool())
client.run(f'{config["KEY"]["key"]}')

