from discord.ext.commands import Bot
import discord
import secret

sthlmesportbot = Bot(command_prefix="!")
client = discord.Client()

@sthlmesportbot.event
async def on_read():
	print("Client logged in")

@sthlmesportbot.command()
async def hello(*args):
	return await sthlmesportbot.say('Hello!')

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

sthlmesportbot.run(secret.BOT_TOKEN)

