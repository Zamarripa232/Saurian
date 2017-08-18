# DiceRolling
# TODO, upper limit rolls, 400 qty, 1000 sides
import random
def dicerolling(qty, sides):
    if qty > 400:
        qty = 1
    if sides > 1000:
        sides = 1
    rolls = []
    genrandoms = []
    start = 1
    totalRoll = 0

    for y in range(sides):
            genrandoms.append(start)
            start += 1
    for i in range(qty):
            random.shuffle(genrandoms)
            rolls.append(genrandoms[random.randint(0,sides-1)])
            random.shuffle(rolls) # makes it appear more random for large amounts of dice rolls
            
    return rolls

def fudgeSingle():
    final = 0
    result = dicerolling(1,6)

    if result[0] in [1, 2]:
        final = 1
    elif result[0] in [3, 4]:
        final = 0
    elif result[0] in [5, 6]:
        final = -1
    return final


def fudgeTranslate(roll):
    translation = ""
    if roll == 1:
        translation = "[+]"
    elif roll == 0:
        translation = "[ ]"
    elif roll == -1:
        translation = "[-]"
    return translation

def fudgeRoll():
    diceFaces = ""
    total = 0
    for i in range(4):
        roll = fudgeSingle()
        total += roll
        diceFaces += fudgeTranslate(roll)
    return [total, diceFaces]

def ladderResult(roll, mod):
    num = roll[0] + mod
    adj = ""

    if num >= 8:
        adj = "Legendary"
    if num == 7:
        adj = "Epic"
    if num == 6:
        adj = "Fantastic"
    if num == 5:
        adj = "Superb"
    if num == 4:
        adj = "Great"
    if num == 3:
        adj = "Good"
    if num == 2:
        adj = "Fair"
    if num == 1:
        adj = "Average"
    if num == 0:
        adj = "Mediocre"
    if num == -1:
        adj = "Poor"
    if num <= -2:
        adj = "Terrible"
    return [num, adj]
