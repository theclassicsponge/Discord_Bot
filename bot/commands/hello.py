import discord
from discord.ext import commands


class Quack(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('Quack command is ready.')

    @commands.command()
    async def hellopablo(self, ctx):
        """The bot replies to the user and displays their name."""
        author = ctx.message.author
        await ctx.send(f'Quack quack {author}!')


def setup(client):
    client.add_cog(Quack(client))