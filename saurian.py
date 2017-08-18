## Saurian.py
import discord, asyncio, random, pickle, os

client = discord.Client()
CHANNEL = '348154337777680385'         # Channel ID can be found by setting discord settings, Appearnce >> Developer Mode
                                       # then right clicking a channel and selecting Copy ID

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def dicerolling(qty, sides):
    rolls = []
    genrandoms = []
    start = 1
    totalRoll = 0

    for y in range(sides):
            genrandoms.append(start)
            start +=1
    for i in range(qty):
            random.shuffle(genrandoms)
            rolls.append(genrandoms[random.randint(0,sides-1)])
            random.shuffle(rolls) # makes it appear more random for large amounts of dice rolls
            
    finalresult = "" + str(rolls) + " total: " + str(totalRoll)
    return rolls


@client.event
async def on_message(message):
    if message.content.startswith('!d6'):
        randd6 = random.randint(1,6)
        await client.send_message(client.get_channel(CHANNEL), randd6)

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
                await client.send_message(client.get_channel(CHANNEL), '' + str(rolls) + ' which resulted in ' + str(successes) + ' successes') 

            # Will roll a set of dice and drop the lowest result, eg D&D stat generation 4d6 drop lowest
            if 'droplow' in argument:
                rolls = dicerolling(qty,sides)
                rolls = sorted(rolls)
                totalRoll = 0
                for i in rolls[:]:
                    totalRoll += i
                totalRoll -= rolls[0]
                
                finalResult = "" + str(rolls) + " total with " + str(rolls[0]) + " dropped: " + str(totalRoll)
                await client.send_message(client.get_channel(CHANNEL), finalResult)

        else:
            rolls = dicerolling(qty,sides)
            totalRoll = 0
            for i in rolls[:]:
                    totalRoll += i
            finalResult = "" + str(rolls) + " total: " + str(totalRoll)
            await client.send_message(client.get_channel(CHANNEL), finalResult)

    elif message.content.startswith('!quit'):
        quit()

#Using with will close the file properly after finishing
with open('token.key','r') as f:
    t = f.read()
    client.run(t)
