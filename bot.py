'''
Created on Aug 16, 2018
@author: yun
'''
import discord
#import logging
from discord.ext.commands import Bot
from discord import Game
import random
from photo_retrieving import dan
from discord.embeds import Embed
import youtube_dl

#logger = logging.getLogger('discord')
#logger.setLevel(logging.DEBUG)
#handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
#handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
#logger.addHandler(handler)

BOT_PREFIX = ("]\\")
TOKEN='NDc5NTUyNDY5MzI0NTI5Njk2.DleAiQ.M07LtLMTEWXcRwgXoeeYoPgWacQ'


client = Bot(command_prefix=BOT_PREFIX)

players = {}

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="ee"))
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('--------------')



@client.command(name='fortune',
                description='Tells you your fortune for the near future.',
                brief='Tells you your fortune for the near future.',
                aliases=['for', '4'],
                pass_context=True)
async def fortune(context):
    fortunes = [
        'You will die in 1 day',
        'You will lose your wallet soon',
        'You will fall down in a couple minutes',
        'You buy food but drop it on the ground within this week',
        'You will be unhappy tomorrow'
    ]
    await client.say(context.message.author.mention + ", " + random.choice(fortunes))

    
@client.command(name='join',
                description = 'Bot joins the voice channel of the user who passed the command',
                brief = 'Bot joins the voice channel of the user who passed the command',
                aliases = ['j'],
                pass_context=True)
async def join(context):
    try:
        channel = context.message.author.voice.voice_channel
        await client.join_voice_channel(channel)
    except:
        await client.say("You need to be in a voice channel for me to join")


@client.command(name = 'leave',
                description = 'Bot leaves the voice channel',
                brief = 'Bot leaves the voice channel',
                aliases = ['l'],
                pass_context=True)
async def leave(context):
    try:
        server = context.message.server
        voice_client = client.voice_client_in(server)
        await voice_client.disconnect()
    except:
        await client.say("I am not in voice channel")

@client.command(pass_context = True)
async def play(context, url):
    
    server = context.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()
    
@client.command()
async def opus():
    await client.say(str(discord.opus.is_loaded()))

@client.command(name='danbooru',
                description='Returns an random image from Danbooru with the given tag',
                brief='Returns a random image from Danbooru with the given tag',
                aliases=['dan'],
                pass_context=True,
                enabled=True)
async def danbooru(context):
    tag = context.message.content
    try:
        item = dan(tag)
        photo = Embed(color = 1162493, description = context.message.author.name + "#" + context.message.author.discriminator + '[' + item[1] + '](' + item[0] + ')')
        photo.set_footer(text = 'Danbooru')
        photo.set_image(url = item[0])
    except:
        photo = Embed(color = 1162493, description = context.message.author.name + "#" + context.message.author.discriminator + " No results found.")
    await client.send_message(destination = context.message.channel, embed = photo)



client.run(TOKEN)







