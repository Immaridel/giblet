import discord
import os
import json
import requests
import random
from replit import db
from keep_alive import keep_alive

# https://www.youtube.com/watch?v=SPTfmiYiuok

client = discord.Client()
# client = discord.Client(description="giblet", command_prefix="-", pm_help = False)

sad_words = ["sad", "depressed", "unhappy", "angry", "mad", "miserable", "depressing"]
starter_encouragements = [
    "Cheer up!",
    "Hang in there!",
    "You are a great person!"
]

if "responding" not in db.keys():
    db["responding"] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]


def delete_encouragements(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself

    if message.author == client.user:
        return

    if message.content.startswith('.gping'):
        msg = 'Oh my God. Fuck off, {0.author.mention}.'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('.gecho'):
        msg = message.content.split(".gecho ", 1)[1]
        await message.channel.send(msg)

    if message.content.startswith('.ghelp'):
        msg = "There's no help to offer.  Fuck off.\nhttps://giphy.com/gifs/QGzPdYCcBbbZm"
        msg2 = "Also, I'm touching myself right now, and you cannot un-know that."
        await message.channel.send(msg)
        await message.channel.send(msg2)

    if message.content.startswith('.inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if db["responding"]:
        options = starter_encouragements
        if "encouragements" in db.keys():
            options = options + list(db["encouragements"])

    if any(word in message.content for word in sad_words):
        await message.channel.send(random.choice(options))
        # await message.channel.send(random.choice(starter_encouragements))

    if message.content.startswith('.add'):
        encouraging_message = message.content.split(".add ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("Encouraging message added.")

    if message.content.startswith('.del'):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(message.content.split(".del", 1)[1])
            delete_encouragements(index)
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if message.content.startswith('.list'):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if message.content.startswith('.responding'):
        value = message.content.split(".responding ", 1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is off.")


@client.event
async def on_ready():
    game = discord.Game("Dicking about")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('-------------------')
    print('Logged in as {0.user}'.format(client))
    # print('Logged in as',client.user.name)
    print('-------------------')


# @client.event
# async def on_ready():
#	print('Logged in as {0.user}'.format(client))

keep_alive()

client.run(os.getenv('TOKEN'))