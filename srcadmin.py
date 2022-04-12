import valve.rcon  # pip install python-valve
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

# Set the bot's prefix, description and wether it sends help in direct messages or not.
client = Bot(description="Srcadmin", command_prefix="-", pm_help=False)


# Post this to console everytime the bot launches.
@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' + str(
        len(client.servers)) + ' servers | Connected to ' + str(len(set(client.get_all_members()))) + ' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__,
                                                                               platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print('--------')
    print('--------')
    print('--------')
    print('--------')
    print('You are running Srcadmin 1.0')
    print('Created by Luke Millanta')
    return await client.change_presence(game=discord.Game(name='Luke Test Bot'))


# Load in your server information
# File should be structured like this: server_name ip_address port password
d = {}
with open("servers.txt") as f:
    for line in f:
        key, *val = line.split()
        d[str(key)] = val


# Post a message in the game server
@client.command()
async def say(server, message):
    v = d.get(server)
    if v is not None:
        address = (v[0], int(v[1]))
        password = v[2]

        with valve.rcon.RCON(address, password) as rcon:
            response = rcon.execute("say " + message)
        print(response.text)

        await client.say("Your message was published in " + server)
        await client.say("Your message: " + message)
    else:
        await client.say(server + " does not exist in your server list.")


# Allow the user to enter custom server commands
@client.command()
async def custom(server, command):
    v = d.get(server)
    if v is not None:
        address = (v[0], int(v[1]))
        password = v[2]

        with valve.rcon.RCON(address, password) as rcon:
            response = rcon.execute(command)
        print(response.text)

        await client.say("Your command was executed on " + server + ".")
    else:
        await client.say(server + " does not exist in your server list.")


# Discord bot user token
client.run('')  # You will need to add your token here