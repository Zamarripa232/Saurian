# Saurian

This is a personal discord bot for twitch.tv/floydasaurus

## Usage
For this bot to work properly, you must create a token.py file in the root directory that will contain your discord app token. You may also want to update the channel IDs within the code after any client.get_channel seen.

## Current commands
**!d6**: rolls a d6 and reports the result to the specified channel id.
**!roll**: rolls a variety of dice. Usage is !roll (Quantity of dice) (number of sides) , eg !roll 1 6 rolls 1d6.

## Additional !roll features ##

* !roll X Y droplow , drops the lowest die value before totalling, similar to D&D character building
* !roll X Y tar=Z , rolls against a target number (equal to or greater than) and counts successes
* !roll dF+X , rolls 4 fudge dice along with modifier. Includes adjectives from The Ladder!
