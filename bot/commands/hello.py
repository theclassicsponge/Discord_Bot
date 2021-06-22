import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import requests
import os


class Quack(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('Quack command is ready.')

    # adds sound
    @commands.command(pass_context=True)
    async def join(self, ctx):
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel.name)
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if not voice.is_connected():
            await voiceChannel.connect()

    @commands.command()
    async def hellopablo(self, ctx):
        """The bot replies to the user and displays their name."""
        author = ctx.message.author
        await ctx.send(f'Quack quack {author}!')


def setup(client):
    client.add_cog(Quack(client))