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
    if message.content.lower().strip().startswith('Jupiter'):
       embed_m = discord.Embed(colour=0x131010)
       embed_m.add_field(name="~",
                         value='\n\n')
       embed_m.set_image(url="https://images.genius.com/02a227b51a5f263b3709ebc76c106200.1000x1000x1.jpg")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()

    #commands:
    elif message.content.lower().strip().startswith(',intro'):
       await message.channel.send('hi <3 just wanted to say i love you.')
       time.sleep(2)
       await message.delete()

client.run(os.getenv("DISCORD_TOKEN"))
