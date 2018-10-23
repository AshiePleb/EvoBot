import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "=")
client.remove_command("help")
@client.event
async def on_ready():
    print("EVO Online!")
    await client.change_presence(game=discord.Game(name="EVO <3"))

@client.event
async def on_message(message):
    if message.content.startswith('=hello'):
        msg = 'Hello {0.author.mention}, How Are You Today? <:EvoBlob1:504249845368750082>'.format(message)
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('=bye'):
        msg = 'GoodBye {0.author.mention}, Hope To See You Again Soon <:EvoBlob1:504249845368750082>'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('=ip'):
        if message.author.id == "475825699123494932":
            msg = '{0.author.mention} The Server IP Is [IP]'.format(message)
            await client.send_message(message.channel, msg)
        else: 
            await client.send_message(message.channel, "Only AntiSepticBoi#9970 Can Run This Command!")
    
    await client.process_commands(message)
   
    if message.content.startswith('=say'):
        args = message.content.split(" ")
        #args[0] = +say
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
             
client.loop.create_task(list_servers())
client.run(os.getenv('TOKEN'))
