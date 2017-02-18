# -*- coding: utf-8 -*-
from discord.ext.commands import Bot
import discord
import secret
import logging
from kommando import kommando_check

#Make sure logging is targetted!
logging.basicConfig(filename='sthlmesportbot.log',level=logging.INFO,format='%(asctime)s %(message)s')

client = discord.Client()
#Make sure dictionary.txt is targetted!
with open('dictionary.txt', 'r') as handle:
    word_list = []
    for line in handle:
        stripped = line.rstrip()
        word_list.append(stripped)

@client.event
async def on_message(message):
    #Profanity Filter
    for word in word_list:
        if message.content.find(word) >= 0:
            user = str(message.author)
            msg = 'Watch your profanity {0.author.mention}!'.format(message)
            await client.send_message(message.channel, msg)
            logging.warning("Message blocked: " + message.content + " From: " + user)
            await client.delete_message(message)
            break
    if message.author == client.user:
       return
    if message.content.startswith('!'):
        is_admin = message.author.permissions_in(message.channel).administrator
        msg = kommando_check(message.content,is_admin).format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    nu_pm = 'Welcome to {0.name}! Make sure to read the rules in <#220934558164451328> . Best Regards, STHLM E-sport'
    await client.send_message(server, fmt.format(member, server))
    await client.send_message(member, nu_pm.format(server))

client.run(secret.BOT_TOKEN)
