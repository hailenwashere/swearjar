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
    if message.content.find('fuck') != -1 :
        print(message.content.find('fuck'))
        print(f'{message.author} said the f word!')
        await message.channel.send('no swearing or steven will eat u')

client.run(TOKEN)