import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


players = {}

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')




@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'robo-dealer, add me':
        if message.author in players:
            players[message.author] += 1
        else:
            players[message.author] = 3
        await message.channel.send(str([str(x) for x in players]))
        await message.channel.send(players[message.author])
        await message.author.send('TEST')
            
#class CustomClient(discord.Client):
#    async def on_ready(self):
#        print(f'{client.user} has connected to Discord!')
    
client.run(TOKEN)
