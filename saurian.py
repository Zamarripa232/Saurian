## Saurian.py
import discord, asyncio, random, pickle, os, lib
from lib.dicerolling import *

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
        await client.send_message(message.channel, randd6)

    if message.content.startswith('!howtotakeovertheworld'):
        await client.send_message(message.channel, 'Floyd can totally help you out with that after large bit donations!')

    # Fudge rolls
    if message.content.startswith('!roll dF'):
        context = message.content
        response = ''
        nummod = 0
        if context[8]=="-":
            mod = context.split('-')
            nummod = -1 * int(mod[1])
        elif context[8]=="+":
            mod = context.split('+')
            nummod = int(mod[1])
        roll = fudgeRoll()
        result = ladderResult(roll, nummod)
        response = ('You rolled {} with {}.\nIncluding the modifier of {} your result is {}, {}!'
                    .format(str(roll[0]),
                    str(roll[1]),
                    str(nummod),
                    str(result[0]),
                    str(result[1])
                    ))
        await client.send_message(message.channel, response)

    elif message.content.startswith('!roll'):
        context = message.content
        split = context.split(' ') # splits at space, e.g. ['!roll', '16', '100']
        qty = int(split[1])
        sides = int(split[2])
        if len(split) == 4:
            argument = split[3]

        ## Checks to see if an argument was appended
        if len(split) == 4:

            # Will compare against a target number to count successes
            if 'tar' in argument:
                successes = 0
                tar = argument.split('=')
                rolls = dicerolling(qty,sides)
                for i in rolls[:]:
                    if i >= int(tar[1]):
                        successes += 1
                await client.send_message(message.channel, '' + str(rolls)[1:-1] + ' which resulted in ' + str(successes) + ' successes') 

            # Will roll a set of dice and drop the lowest result, eg D&D stat generation 4d6 drop lowest
            if 'droplow' in argument:
                rolls = dicerolling(qty,sides)
                rolls = sorted(rolls)
                totalRoll = 0
                for i in rolls[:]:
                    totalRoll += i
                totalRoll -= rolls[0]
                
                finalResult = "" + str(rolls)[1:-1] + " total with " + str(rolls[0]) + " dropped: " + str(totalRoll)
                await client.send_message(message.channel, finalResult)

        else:
            rolls = dicerolling(qty,sides)
            totalRoll = 0
            for i in rolls[:]:
                    totalRoll += i
            finalResult = "" + str(rolls)[1:-1] + " total: " + str(totalRoll)
            await client.send_message(message.channel, finalResult)

    elif message.content.startswith('!quit'):
        quit()

#Using with will close the file properly after finishing
with open('token.key','r') as f:
    t = f.read()
    client.run(t)
