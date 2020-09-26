# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client()
bot = commands.Bot(command_prefix = '$')

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

#@client.event
#async def on_ready():
#    print(f'{client.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if (message.author.bot):
        return
    userindex = -1

    for i in range(len(swears)):
        if message.content.find(swears[i]) != -1:
            for j in range(len(userswear)):
                if message.author.name == userswear[j]:
                    userindex = j
                #print(userswear[j])
    
            if userindex == -1:
                userswear.append(message.author.name)
                swearcounter.append([0]*len(swears))
                userindex = len(userswear) - 1

            (swearcounter[userindex])[i] += 1

            #print(message.content.find(swears[i]))

            #print(f'{message.author.name} said the {swears[i]} word!')

            #print(f'{userswear[userindex]} {(swearcounter[userindex])[i]}')

            await message.channel.send(
                f'{message.author.nick} said the {swears[i][0]} word! you\'ve said the {swears[i][0]} word {(swearcounter[userindex])[i]} time(s)! **no swearing or steven will eat u**'
            )

    await bot.process_commands(message)

@bot.command(name = 'save')
async def save(ctx):
    f = open('userswear.txt', 'w')
    
    #for user in userswear:
    #print(userswear)

    f.write('\n'.join(userswear))
    # *userswear, sep='\n'


    f.close()

    f = open('realswearjar.txt','w')
    f.write('\n'.join([' '.join([str(num) for num in line]) for line in swearcounter]))
    f.close()

    f = open('swears.txt', 'w')
    f.write('\n'.join(swears))
    f.close()

    await ctx.send('saved!')

@bot.command(name = 'register')
@commands.is_owner()
async def register(ctx, swear):
    for s in swears:
        if (s == swear):
            await ctx.send(f'{swear} is already a swear word dumbass')
            return
    swears.append(swear)
    for arr in swearcounter:
        arr.append(0)

    await ctx.send(f'{swear} registered. **steven is watching**')

@bot.command(name = 'stats')
async def stats(ctx, member: discord.Member, arg):
    userindex = -1
    for i in range(len(userswear)):
        if (userswear[i] == member.name):
            userindex = i
            break
    if (userindex == -1):
        await ctx.send(f'{member.nick} has not sworn. they will not suffer the wrath of steven')
        return

    if (arg == 'all'):
        pass
    else:
        swearindex = -1
        for i in range(len(swears)):
            if (swears[i] == arg):
                swearindex = i
                break
        if (swearindex == -1):
            await ctx.send(f'{arg} is not a swear word')
            return

        await ctx.send(f'{member.nick} has said the {arg[0]} word {swearcounter[userindex][swearindex]} time(s)')
        
bot.run(TOKEN)
#client.run(TOKEN)
