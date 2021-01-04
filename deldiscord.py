import discord
import asyncio
import sys

client = discord.Client()

@client.event
async def on_ready():
	print("[+] " + client.user.name + " logged in")
	if len(sys.argv) > 1:
		for channelid in sys.argv[1:]:
			if not channelid.isdigit(): continue

			channel = client.get_channel(int(channelid))
			if channel != None: name = channel.name
			if channel == None:
				channel = client.get_user(int(channelid)).dm_channel
				name = channel.recipient.name
				if channel == None:
					print('[-] ' + channelid + ' is not a valid channel')
					continue

			print('[?] deleting messages from ' + name)
			c = 0
			async for msg in channel.history(limit=None):
				if msg.author == client.user:
					await msg.delete()
					print('[?] deleted ' + msg.content)
					c += 1
			print('[+] done deleting ' + str(c) + ' messages')

def is_me(m):
	return m.author == client.user

@client.event
async def on_message(m):
	if m.author.id == client.user.id and m.content == ".d":
		await m.delete()
		c = 0
		async for msg in m.channel.history(limit=None):
			if msg.author == client.user:
				await msg.delete()
				c += 1
		print('[+] done deleting ' + str(c) + ' messages')


client.run("censored", bot=False)
