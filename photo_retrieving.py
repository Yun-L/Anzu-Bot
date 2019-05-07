'''

Author: yun

'''
import discord
from pybooru import Danbooru
from discord.ext import commands

class Photos(commands.Cog):
    def __init__(self, bot):
        self.bot = commands.bot
        self.danbooru_client = Danbooru(site_name = 'danbooru')

    def _get_url_list_danbooru(self, tag, request_number):
        posts = self.danbooru_client.post_list(limit = request_number,
                                               tags = tag,
                                               random = True) 
        pictures = []

        for post in posts:
            pictures += [post['file_url']]

        return pictures

    @commands.command()
    async def unleash_load_danbooru(self, ctx, arg1):

        urls = self._get_url_list_danbooru(arg1, 5)

        # Check if at least 1 image is found
        if urls == []:
            await ctx.send('no images found')
            return
        
        fmt = ""

        for url in urls:
            fmt += url + "\n"

        await ctx.send(fmt)

    @commands.command()
    async def danbooru(self, ctx, arg1):

        urls = self._get_url_list_danbooru(arg1, 1)

        # construct embedded image
        discord_embed = discord.Embed(colour = 0x4286f4)
        discord_embed.set_author(name = arg1)
        discord_embed.set_footer(text = ctx.message.author)

        # check if danbooru tag returns url
        if urls == []:
            discord_embed.title = 'No image found'
        else:
            discord_embed.set_image(url = urls[0])

        try:
            await ctx.send(embed = discord_embed)
        except:
            print('send failed')
            print(discord_embed.to_dict())

                

def setup(bot):
    bot.add_cog(Photos(bot))

