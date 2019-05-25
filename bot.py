'''

Author: Yun

'''
import discord
import configparser
import logging
from discord.ext import commands

logging.basicConfig(level=logging.INFO)

config = configparser.ConfigParser()
config.read('config.ini')

PREFIX = config['Default']['Prefix']
TOKEN = config['Default']['Token']

bot = commands.Bot(command_prefix=PREFIX)
extensions = ['music', 'photo_retrieving']


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="ee"))
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('With bot prefix: {}'.format(PREFIX))
    print('--------------')


if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('{} could not be loaded: {}'.format(extension, e))

    bot.run(TOKEN)
