import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import asyncio
import os

startup_extensions = ["Music"]
bot = commands.Bot("-")
bot.remove_command("help")
@bot.event
async def on_ready():
    print("bot online")

class Main_Commands():
        def __init__(self, bot):
         self.bot = bot

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="My Commands", description="Here Are My Commands, My Prefix Is `-`", color=0xff00ff)
    embed.add_field(name="resume", value="Resumes the currently played song.", inline=False)
    embed.add_field(name="join", value="Joins a voice channel.", inline=False)
    embed.add_field(name="volume", value="Sets the volume of the currently playing song.", inline=False)
    embed.add_field(name="summon", value="Summons the bot to join your voice channel.", inline=False)
    embed.add_field(name="stop", value="Stops laying audio and leaves the voice channel.", inline=False)
    embed.add_field(name="skip", value="Vote to skip a song. The song requester can automatically skip.", inline=False)
    embed.add_field(name="playing", value="Shows info about the currently played song.", inline=False)
    embed.add_field(name="play", value="Plays a song.", inline=False)
    embed.add_field(name="invite", value="Gives you my invite URL.", inline=False)
    await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(title="Invite", description="Invite me to your discords!", color=0xff00ff)
    embed.add_field(name="Here is my invite link", value="https://discordapp.com/api/oauth2/authorize?client_id=517827745409925151&permissions=8&scope=bot", inline=False)
    await bot.say(embed=embed)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.fortmat(extension, exc))

client.run(os.getenv('TOKEN'))
