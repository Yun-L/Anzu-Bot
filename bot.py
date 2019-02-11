'''
Created on Aug 16, 2018

@author: yun
'''

import discord
from discord.ext import commands


PREFIX = ']\\'
TOKEN = 'NDc5NTUyNDY5MzI0NTI5Njk2.DleAiQ.M07LtLMTEWXcRwgXoeeYoPgWacQ'


bot = commands.Bot(command_prefix = PREFIX)
extensions = ['music', 'photo_retrieving']

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="ee"))
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------')


if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('{} could not be loaded: {}'.format(extension, e))

    bot.run(TOKEN)

