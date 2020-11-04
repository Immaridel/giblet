# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import os
import discord
import asyncio
import platform
#import mcrcon
from discord.ext import commands
from discord.ext.commands import Bot

#TOKEN = "NDcyMjA4NzM4NjYxNDMzMzQ1.DjwC2Q.6luhJbgkN1NjAUBxr0Yn5-82DFI"
TOKEN = "NDcyMjA4NzM4NjYxNDMzMzQ1.W1pwqA.H0-nE4NW8JHQfUvioElIxtCgtHc"

#client = discord.Client()
client = Bot(description="giblet", command_prefix="-", pm_help = False)

@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return

	if message.content.startswith('gb ping'):
		msg = 'Oh my God. Fuck off, {0.author.mention}.'.format(message)
		await message.channel.send(msg)

	if message.content.startswith('gb echo'):
		msg = message.content
		await message.channel.send(message.channel, msg)

	if message.content.startswith('gb help'):
		msg = "There's no help to offer.  Fuck off.\nhttps://giphy.com/gifs/QGzPdYCcBbbZm"
		msg2 = "Also, I'm touching myself right now, and you cannot un-know that."
		await message.channel.send(message.author, msg)
		await message.channel.send(message.author, msg2)

@client.event
async def on_ready():
	game = discord.Game("Dicking about")
	await client.change_presence(status=discord.Status.idle, activity=game)
	print('-------------------')
	print('Logged in as',client.user.name)
	print('-------------------')

client.run(TOKEN)