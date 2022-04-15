import discord
import os
import time

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.Invisible, activity=discord.Activity(type=discord.ActivityType.listening, name="Flower Face")) 


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #embed:
    if message.content.lower().strip().startswith('command'):
       embed_m = discord.Embed(colour=0x33802f)
       embed_m.add_field(name="~",
                         value='\n\n')
       embed_m.set_image(url="cute picture")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()

    #commands:
    elif message.content.lower().strip().startswith(',intro'):
       await message.channel.send('hi <3 just wanted to say i love you.')
       time.sleep(2)
       await message.delete()

client.run(os.getenv("DISCORD_TOKEN"))
