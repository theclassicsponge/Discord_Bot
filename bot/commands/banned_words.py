import discord
import random
from discord.ext import commands

class BannedWords(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Banned Words command is work in progress.')

def setup(client):
    client.add_cog(BannedWords(client))
