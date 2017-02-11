from discord.ext.commands import Bot
import discord
import secret
import logging

logging.basicConfig(level=logging.INFO)

#sthlmesportbot = Bot(command_prefix="!")
client = discord.Client()

#@sthlmesportbot.event
#async def on_read():
#	print("Client logged in")

#@sthlmesportbot.command()
@client.event
async def on_message(message):
	if message.author == client.user:
 	   return
	if message.content.startswith('!hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)
	#return await sthlmesportbot.say('Hello!' message.author.mention)

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    nu_pm = 'Welcome to {0.name}! Make sure to read the rules in <#220934558164451328> . Best Regards, STHLM E-sport'
    await client.send_message(server, fmt.format(member, server))
    await client.send_message(member, nu_pm.format(server))
client.run(secret.BOT_TOKEN)

