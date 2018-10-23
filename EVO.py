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
            
    if message.content.startswith('=invite'):
        if message.author.id == "475825699123494932":
            msg = 'https://discordapp.com/api/oauth2/authorize?client_id=499643998194106369&permissions=0&scope=bot'.format(message)
            await client.send_message(message.channel, msg)
        else: 
            await client.send_message(message.channel, "Only AntiSepticBoi#9970 Can Run This Command!")            
   
    if message.content.startswith('/infomation'):
      embed = discord.Embed(title="EVO Server Infomation", color=0xff00ff)
      embed.add_field(name="<:EvoDiamond:504246347298242573> IP <:EvoDiamond:504246347298242573>", value="<:EvoBlob1:504249845368750082> Coming Soon! <:EvoBlob1:504249845368750082>", inline=False)
      embed.add_field(name="<:EvoDiamond:504246347298242573> Forum <:EvoDiamond:504246347298242573>", value="<:EvoBlob1:504249845368750082> http://evonetwork.ga/ <:EvoBlob1:504249845368750082>", inline=False)
      embed.add_field(name="<:EvoDiamond:504246347298242573> Discord <:EvoDiamond:504246347298242573>", value="<:EvoBlob1:504249845368750082> https://discord.gg/zRh8WP6 <:EvoBlob1:504249845368750082>", inline=False)
      embed.add_field(name="<:EvoDiamond:504246347298242573> Vote <:EvoDiamond:504246347298242573>", value="<:EvoBlob1:504249845368750082> https://minecraftpocket-servers.com/server/80563/vote/ <:EvoBlob1:504249845368750082>", inline=False)  
      await client.send_message(message.channel, embed=embed)    

    if message.content.startswith('=say'):
        args = message.content.split(" ")
        #args[0] = +say
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
             
client.run(os.getenv('TOKEN'))
