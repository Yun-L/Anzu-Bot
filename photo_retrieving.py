'''
Created on Aug 21, 2018

@author: yun
'''
import discord
from pybooru import Danbooru
from discord.ext import commands
from discord.ext.commands import bot

class Pictures:
    def __init__(self, bot):
        self.bot = bot
        self.danbooru_client = Danbooru(site_name = 'danbooru')

    def get_url_list_danbooru(self, tag, request_number):
        posts = self.danbooru_client.post_list(limit = request_number, \
                                               tags = tag, \
                                               random = True) 
        pictures = []

        for post in posts:
            pictures += [post['file_url']]

        return pictures

    @commands.command(pass_context = True)
    async def unleash_load_danbooru(self, ctx, arg1):

        urls = self.get_url_list_danbooru(arg1, 5)

        fmt = ""

        for url in urls:
            fmt += url + "\n"

        await self.bot.say(fmt)

    @commands.command(pass_context = True)
    async def danbooru(self, ctx, arg1):

        urls = self.get_url_list_danbooru(arg1, 1)

        for url in urls:
            discord_embed = discord.Embed(colour = 0x4286f4)
            
            discord_embed.set_image(url = url)
            discord_embed.set_author(name = arg1)
            discord_embed.set_footer(text = ctx.message.author)

            try:
                await self.bot.send_message(destination = ctx.message.channel, embed = discord_embed)
            except:
                print('w')
            print(discord_embed.to_dict())


def setup(bot):
    bot.add_cog(Pictures(bot))
    
