import discord
import os
import time

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name="Flower Face")) 


@client.event
async def on_message(message):
    if message.author == client.user:
        return

#embed:

    elif message.content.lower().strip().startswith(''):
       await message.channel.send('')
       time.sleep(2)
       await message.delete()

    if message.content.lower().strip().startswith(''):
       embed_m = discord.Embed(colour=0x89658d)
       embed_m.add_field(name="~",
                         value='')
       embed_m.set_image(url="")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()

#commands:


    elif message.content.lower().strip().startswith(''):
       await message.channel.send('')
       time.sleep(2)
       await message.delete()

    if message.content.lower().strip().startswith(''):
       embed_m = discord.Embed(colour=0x89658d)
       embed_m.add_field(name="~",
                         value='')
       embed_m.set_image(url="")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()


client.run(os.getenv("DISCORD_TOKEN"))
