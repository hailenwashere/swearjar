# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

f = open('swears.txt','r')
swears = f.read()
swears = swears.split('\n') 

f = open('userswear.txt','r')
userswear = f.read()
userswear = userswear.split('\n')

f = open('realswearjar.txt','r')
swearcounter = f.read()
swearcounter = swearcounter.split('\n')
for i in range(len(swearcounter)):
    swearcounter[i] = list(map(int, swearcounter[i].split(' ')))

print(userswear, swearcounter, swears)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message): 

    userindex = -1

    for i in range(len(swears)):
        if message.content.find(swears[i]) != -1:
            for j in range(len(userswear)):
                if message.author.name == userswear[j]:
                    userindex = j
                print(userswear[j])
    
            if userindex == -1:
                userswear.append(message.author.name)
                swearcounter.append([0]*len(swears))
                userindex = len(userswear) - 1

            (swearcounter[userindex])[i] += 1

            print(message.content.find(swears[i]))

            print(f'{message.author.name} said the {swears[i]} word!')

            print(f'{userswear[userindex]} {(swearcounter[userindex])[i]}')

            await message.channel.send(
                f'@{message.author} said the {swears[i][0]} word! you\'ve said the {swears[i][0]} word {(swearcounter[userindex])[i]} time(s)! **no swearing or steven will eat u**'
            )

    if message.content == '$save':
        f = open('userswear.txt', 'w')
        
        #for user in userswear:
        print(userswear)

        f.write('\n'.join(userswear))
        # *userswear, sep='\n'


        f.close()

        f = open('realswearjar.txt','w')

        """for line in swearcounter:
            for num in line:
                f.write(str(num)+' ')
            f.write('\n')"""

        f.write('\n'.join([' '.join([str(num) for num in line]) for line in swearcounter]))

        f.close()

        await message.channel.send('saved!')

client.run(TOKEN)
