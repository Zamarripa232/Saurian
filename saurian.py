## Saurian.py
import discord, asyncio, random, pickle, os

client = discord.Client()
CHANNEL = '348154337777680385'

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

## test of just rolling a d6
@client.event
async def on_message(message):
    if message.content.startswith('!d6'):
        randd6 = random.randint(1,6)
        # Channel ID can be found by setting discord settings, Appearnce >> Developer Mode
        # then right clicking a channel and selecting Copy ID
        await client.send_message(client.get_channel('348154337777680385'), randd6)

    elif message.content.startswith('!roll'):
        context = message.content
        split = context.split(' ') # splits at space, e.g. ['!roll', '16', '100']
        qty = int(split[1])
        sides = int(split[2])
        if len(split) == 4:
            argument = split[3]

        if len(split) == 4:
            if 'tar' in argument:
                await client.send_message(client.get_channel(CHANNEL), 'Testing target number stuff') # TODO

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
