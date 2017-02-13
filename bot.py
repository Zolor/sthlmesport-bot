from discord.ext.commands import Bot
import discord
import secret
import logging

#Make sure logging is targetted!
logging.basicConfig(filename='log/sthlmesportbot.log',level=logging.INFO,format='%(asctime)s %(message)s')

client = discord.Client()
#Make sure dictionary.txt is targetted!
with open('dictionary.txt', 'r') as handle:
    word_list = []
    for line in handle:
        stripped = line.rstrip()
        word_list.append(stripped)

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
       return
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!måndag'):
        msg = 'Snart är det Lördag igen!~'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!tisdag'):
        msg = 'T-3 dagar kvar tills !Fredagsmys !'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!onsdag'):
        msg = 'Lill-Lördag!'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!torsdag'):
        msg = 'Fredag imorgon! Redo för !Fredagsmys ??'.format(message)
        await client.send_message(message.channel,msg)
    if message.content.find('!fredag') >= 0:
        msg = 'På Fredagar är det Fredagsmys!'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!lördag'):
        msg = 'Snart är det Måndag igen!~'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!söndag'):
        msg = 'Gaming Day \o/'.format(message)
        await client.send_message(message.channel, msg)
#Profanity Filter
    for word in word_list:
        if message.content.find(word) >= 0:
            user = str(message.author)
            msg = 'Watch your profanity {0.author.mention}!'.format(message)
            await client.send_message(message.channel, msg)
            logging.warning("Message blocked: " + message.content + " From: " + user)
            await client.delete_message(message)
            break


@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    nu_pm = 'Welcome to {0.name}! Make sure to read the rules in <#220934558164451328> . Best Regards, STHLM E-sport'
    await client.send_message(server, fmt.format(member, server))
    await client.send_message(member, nu_pm.format(server))

client.run(secret.BOT_TOKEN)