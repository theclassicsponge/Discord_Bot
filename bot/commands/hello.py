import discord

@client.event
async def on_ready():
    print('You have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'general':
        if user_message.lower() == '!hellopablo':
            await message.channel.send(f'Quack Quack {username}.')
            return
