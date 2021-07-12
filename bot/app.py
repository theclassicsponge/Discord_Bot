import discord
import os
from discord.ext import commands
import urllib.parse, urllib.request, re
import configparser

client = commands.Bot(command_prefix="!")
client.remove_command('help')
config = configparser.ConfigParser()
config.read('keys.ini')


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

client.run(f'{config["KEY"]["key"]}')

