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
    if message.content.lower().strip().startswith('.Jupiter'):
       embed_m = discord.Embed(colour=0x131010)
       embed_m.add_field(name="~",
                         value='hihihi')
       embed_m.set_image(url="https://images.genius.com/02a227b51a5f263b3709ebc76c106200.1000x1000x1.jpg")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()


#commands:
    elif message.content.lower().strip().startswith('.question'):
       await message.channel.send('https://open.spotify.com/track/7crSKtI09erdDYWLLsP4vi?si=22dddaea3eef4eac')

    elif message.content.lower().strip().startswith('!question'):
       await message.channel.send('https://open.spotify.com/track/7hfi4ZTfV7akmGINh6qYCF?si=848c7ccdbe40411f')

    elif message.content.lower().strip().startswith('@question'):
       await message.channel.send('https://open.spotify.com/track/1IxfE1rd0ngSFP8MSqYiv0?si=b9aa847b86cb4c43')

    elif message.content.lower().strip().startswith('$question'):
       await message.channel.send('https://open.spotify.com/track/3U21A07gAloCc4P7J8rxcn?si=e9f656d468234c54')

    elif message.content.lower().strip().startswith('*question'):
       await message.channel.send('https://open.spotify.com/track/3zWR0zS9p39c0FVkYkHfVF?si=4bebb8580afb480b')

    elif message.content.lower().strip().startswith('^question'):
       await message.channel.send('https://open.spotify.com/track/3zWR0zS9p39c0FVkYkHfVF?si=4bebb8580afb480b')

    elif message.content.lower().strip().startswith('#question'):
       await message.channel.send('https://open.spotify.com/track/63vr7fhaIB6Zq7YOJ1xqJm?si=b71f96b22bb348e0')




client.run(os.getenv("DISCORD_TOKEN"))
