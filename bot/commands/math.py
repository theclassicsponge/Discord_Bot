import discord
from discord.ext import commands


class Math(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Math command is ready.')

    @commands.command()
    async def mul(self, ctx, num1: int, num2: int):
        """Multiplies two given numbers."""
        await ctx.send(num1*num2)

    @commands.command()
    async def add(self, ctx, num1: int, num2: int):
        """Finds the sum of two given numbers."""
        await ctx.send(num1+num2)

    @commands.command()
    async def sub(self, ctx, num1: int, num2: int):
        """Subtracts two given numbers."""
        await ctx.send(num1-num2)



def setup(client):
    client.add_cog(Math(client))