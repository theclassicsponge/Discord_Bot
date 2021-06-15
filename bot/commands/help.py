import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help command is ready.')

    @commands.command(pass_context=True)
    async def help(self, ctx):
        """Custom help command that displays a list of bot commands and what the command does."""
        embed = discord.Embed(
            colour=discord.Colour.blue()
        )

        embed.set_author(name='Help:')
        embed.add_field(name='!ping', value='Returns Pong!', inline=False)
        embed.add_field(name='!hellopablo', value='Pablo quacks at you.', inline=False)
        embed.add_field(name='!mul', value='Multiplies two given integers. I.e. !mul 2 2 displays 4.', inline=False)
        embed.add_field(name='!add', value='Finds the sum of two given numbers. I.e. !add 2 1 displays 3.', inline=False)
        embed.add_field(name='!sub', value='Subtracts two given numbers. I.e. !sub 3 1 displays 2.', inline=False)
        embed.add_field(name='!youtube', value='Displays a youtube video. I.e. !youtube never gonna give you up displays '
        'http://www.youtube.com/watch?v=dQw4w9WgXcQ.', inline=False)
        embed.add_field(name='!load <cog name>', value='Loads a cog.', inline=False)
        embed.add_field(name='!unload <cog name>', value='unloads a cog.', inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
