import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'beep':
        await message.channel.send('boop')

    if message.content == 'cards':
        await message.channel.send('🂳 🂴 🂵 ')
            

#class CustomClient(discord.Client):
#    async def on_ready(self):
#        print(f'{client.user} has connected to Discord!')
    
client.run(TOKEN)
