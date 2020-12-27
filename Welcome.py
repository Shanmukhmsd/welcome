import discord
from discord import Game 
from discord.ext import commands 
from discord.ext.commands import Bot 
import asyncio 

client=commands.Bot (command_prefix="+") 
client.remove_command("help") 

@client.event 
async def on_ready():
     print("created by shanmukh ©®⁷")
     print(client.user.name)
     print("--------")
     
@client.event 
async def on_member_join(member):
     embed=discord.Embed(title="Welcome!",colour=0x9208ea,description=f"{member.mention} Just Joined /nwelcome to our server have a nice day 
     embed.set_footer(text="Made by shanmukh")

      msg = await cilent.send_message(discord.object(id="792618358213967945")embed=embed) 
     
     
@client.command(pass_context=True)
async def hello(ctx):
     await client.say("Hello :Partying_face:")
     
     
client.run("NzkyNjQ4MTY3NzgyNzQ0MDg1.X-gxIQ.HEiLOrMLRlfdCJNOa3IOMYIutNg")
