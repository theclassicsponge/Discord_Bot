import discord
from discord.ext import commands
import urllib.parse, urllib.request, re
import time

class Youtube(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Youtube command is ready.')

    @commands.command()
    async def youtube(self, ctx, *, search):
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

    @commands.command()
    async def youtubechan(self, ctx, amount=1):
        """Takes a user input and displays the first youtube channel based on the input DOES NOT WORK."""
        # add *, search
        await ctx.send("This Command is Coming Soon!")
        time.sleep(5)
        await ctx.channel.purge(limit=amount)
        # query_string = urllib.parse.urlencode({
        #     'search_query': search
        # })
        # htm_content = urllib.request.urlopen(
        #     f'http://www.youtube.com/results?search_query={query_string}'
        # )
        #
        # search_results = re.findall(r"https://www.youtube.com/user/(\S{11})", htm_content.read().decode())
        # await ctx.send(f'https://www.youtube.com/results?search_query={search_results[0]}&sp=EgIQAg%253D%253D')
        # # displays one search result

def setup(client):
    client.add_cog(Youtube(client))