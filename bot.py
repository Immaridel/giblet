import discord
import os
import asyncio
#import platform
#import mcrcon
#from discord.ext import commands
#from discord.ext.commands import Bot

#client = discord.Client()
client = discord.Client(description="giblet", command_prefix="-", pm_help = False)

@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return

	if message.content.startswith('.gping'):
		msg = 'Oh my God. Fuck off, {0.author.mention}.'.format(message)
		await message.channel.send(msg)

	if message.content.startswith('.gecho'):
		msg = message.content
		await message.channel.send(msg)

	if message.content.startswith('.ghelp'):
		msg = "There's no help to offer.  Fuck off.\nhttps://giphy.com/gifs/QGzPdYCcBbbZm"
		msg2 = "Also, I'm touching myself right now, and you cannot un-know that."
		await message.channel.send(msg)
		await message.channel.send(msg2)

@client.event
async def on_ready():
	game = discord.Game("Dicking about")
	await client.change_presence(status=discord.Status.idle, activity=game)
	print('-------------------')
	print('Logged in as {0.user}'.format(client))
  #print('Logged in as',client.user.name)
	print('-------------------')

#@client.event
#async def on_ready():
#	print('Logged in as {0.user}'.format(client))

client.run(os.getenv('TOKEN'))