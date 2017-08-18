## Saurian.py
import discord, asyncio, random, pickle, os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!d6'):
        randd6 = random.randint(1,6)
        # Channel ID can be found by setting discord settings, Appearnce >> Developer Mode
        # then right clicking a channel and selecting Copy ID
        await client.send_message(client.get_channel('348154337777680385'), randd6)

#Using with will close the file properly after finishing
with open('token.key') as f:
    t = f.read()
    client.run(t)
