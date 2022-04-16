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

    elif message.content.lower().strip().startswith(',info'):
       await message.channel.send('`react with .jupiter`')
       time.sleep(2)
       await message.delete()

    if message.content.lower().strip().startswith('.jupiter'):
       embed_m = discord.Embed(colour=0x89658d)
       embed_m.add_field(name="~",
                         value='i love you.')
       embed_m.set_image(url="https://media.discordapp.net/attachments/964663907463602206/964754029974532146/Screen_Shot_2022-04-16_at_1.08.00_AM.png")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()

#commands:
    elif message.content.lower().strip().startswith(',1'):
       await message.channel.send('https://open.spotify.com/track/7crSKtI09erdDYWLLsP4vi?si=22dddaea3eef4eac')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',2'):
       await message.channel.send('https://open.spotify.com/track/7hfi4ZTfV7akmGINh6qYCF?si=848c7ccdbe40411f')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',3'):
       await message.channel.send('https://open.spotify.com/track/1IxfE1rd0ngSFP8MSqYiv0?si=b9aa847b86cb4c43')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',4'):
       await message.channel.send('https://open.spotify.com/track/3U21A07gAloCc4P7J8rxcn?si=e9f656d468234c54')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',5'):
       await message.channel.send('https://open.spotify.com/track/3zWR0zS9p39c0FVkYkHfVF?si=4bebb8580afb480b')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',6'):
       await message.channel.send('you\'re aware im asking you out, yes?')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',proud'):
       await message.channel.send('im just so proud of you. words can\'t describe.')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',other'):
       await message.channel.send('I want to lay on the kitchen floor with you\n\nI want to do all the things that lovers do\n\nBruised on your face like a watercolour bloom\n\nMoonlight paints your skin... cornflower blue')
       time.sleep(2)
       await message.delete()




client.run(os.getenv("DISCORD_TOKEN"))
