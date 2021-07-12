import discord
import random
from discord.ext import commands

badwords = ['bad', 'words', 'here']

class BannedWords(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Banned Words command is ready.')



    @commands.Cog.listener()
    async def on_message(self, message):
        for i in badwords:  # Go through the list of bad words;
            if i in message:
                await message.delete()
                await message.channel.send(f"{message.author.mention} Don't use that word here!")
                return  # So that it doesn't try to delete the message again.





def setup(client):
    client.add_cog(BannedWords(client))