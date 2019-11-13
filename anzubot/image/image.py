import discord
from discord.ext import commands


class Image(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def danbooru(self, ctx):
        return "TODO"

    @commands.command()
    async def gelbooru(self, ctx):
        return "TODO"

    @commands.command()
    async def moebooru(self, ctx):
        return "TODO"
