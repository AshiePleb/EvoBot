import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from discord.utils import get
import time
import os
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "%")
client.remove_command("help")
@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(game=discord.Game(name="%help | EVO <3"))
    await asyncio.sleep(10)
    await client.change_presence(game=discord.Game(name="%help | PolyBalls <3"))
    await asyncio.sleep(10)
    await client.change_presence(game=discord.Game(name="%help | Jack <3"))
    await asyncio.sleep(10)
    await client.change_presence(game=discord.Game(name="%help | TheDeibo <3"))
    await asyncio.sleep(10) 

    
@client.event
async def on_message(message):
    if message.content.startswith('hello'):
        msg = 'Hello {0.author.mention}, How Are You Today? <:EvoBlob1:504249845368750082>'.format(message)
        await client.send_message(message.channel, msg)      
        
    if message.content.startswith('bye'):
        msg = 'GoodBye {0.author.mention}, Hope To See You Again Soon <:EvoBlob1:504249845368750082>'.format(message)
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('<@504587557045141514>'):
        msg = '{0.author.mention}, Why you tagging me <:PeepoPinnged:501412813101858836>'.format(message)
        await client.send_message(message.channel, msg) 
        
    if message.content.startswith('<@493883172027760661>'):
        msg = 'Jack is currently AFK he will respond soon! <:EvoBlob2:504721901067829248>'.format(message)
        await client.send_message(message.channel, msg)         
 
    if message.content.startswith('%invite'):
        if message.author.id == "493883172027760661":
            msg = '[Need to update the url]'.format(message)
            await client.send_message(message.channel, msg)
        else: 
            await client.send_message(message.channel, ":x: Error! You must be the bot owner to run this command!")                      

    if message.content.startswith('%info'):
      embed = discord.Embed(title="EVO Server Infomation", color=0xff00ff)
      embed.add_field(name="<:EvoDiamond:504246347298242573> IP <:EvoDiamond:504246347298242573>", value="<:EvoBlob1:504249845368750082> Coming Soon! <:EvoBlob1:504249845368750082>", inline=False)
      embed.add_field(name="<:EvoDiamond:504246347298242573> Forum <:EvoDiamond:504246347298242573>", value="<:EvoBlob1:504249845368750082> http://evonetwork.ga/ <:EvoBlob1:504249845368750082>", inline=False)
      embed.add_field(name="<:EvoDiamond:504246347298242573> Discord <:EvoDiamond:504246347298242573>", value="<:EvoBlob1:504249845368750082> https://discord.gg/zRh8WP6 <:EvoBlob1:504249845368750082>", inline=False)
      embed.add_field(name="<:EvoDiamond:504246347298242573> Vote <:EvoDiamond:504246347298242573>", value="<:EvoBlob1:504249845368750082> https://minecraftpocket-servers.com/server/80563/vote/ <:EvoBlob1:504249845368750082>", inline=False)  
      await client.send_message(message.channel, embed=embed)    
        
    if message.content.startswith('%help'):
      embed = discord.Embed(title="EVO Bot Commands", description="Bot Prefix `%`", color=0xff00ff)
      embed.add_field(name="<:EvoDiamond:504246347298242573> hello <:EvoDiamond:504246347298242573>", value="<:EvoBlob1:504249845368750082> Triggers when you say hello <:EvoBlob1:504249845368750082>", inline=False)
      embed.add_field(name="<:EvoDiamond:504246347298242573> bye <:EvoDiamond:504246347298242573>", value="<:EvoBlob1:504249845368750082> Triggers when you say bye <:EvoBlob1:504249845368750082>", inline=False)
      embed.add_field(name="<:EvoDiamond:504246347298242573> say <:EvoDiamond:504246347298242573>", value="<:EvoBlob1:504249845368750082> Makes the bot say something when you use %say msg <:EvoBlob1:504249845368750082>", inline=False)
      embed.add_field(name="<:EvoDiamond:504246347298242573> info <:EvoDiamond:504246347298242573>", value="<:EvoBlob1:504249845368750082> Lists the EVO Servers infomation <:EvoBlob1:504249845368750082>", inline=False) 
      await client.send_message(message.channel, embed=embed) 
    
@bot.command(pass_context=True)
async def say(ctx, *, msg):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '493883172027760661':
             await bot.delete_message(ctx.message)
             await bot.send_message(ctx.message.channel, msg)
    else:
            await bot.say(":x: Error! You must have administrator permission!")

client.run(os.getenv('TOKEN'))
