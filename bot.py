'''
Created on Aug 16, 2018

@author: yun
'''

import discord
import configparser
from discord.ext import commands

config = configparser.ConfigParser()
config.read('config.ini')

PREFIX = config['Default']['Token']
TOKEN = config['Default']['Token']


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

