# bot.py
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
    f = open('swears.txt','r')
    swears = f.read()
        # swears = 'fuck\nbitch\nshit' 
    swears = swears.split('\n') 
     
    for line in swears:
        if message.content.find(line) != -1 :
            print(message.content.find(line))
            print(f'{message.author} said the {line[0]} word!')
            await message.channel.send(f'@{message.author} said the {line[0]} word! no swearing or steven will eat u')

client.run(TOKEN)
