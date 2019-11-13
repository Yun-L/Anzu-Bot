import discord
from discord.ext import commands


class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.players = {}

    @commands.command()
    async def play(self, ctx):
        await ctx.send("TODO")
        return

    @commands.command()
    async def leave(self, ctx):
        await ctx.send("TODO")
        return

    @commands.command()
    async def join(self, ctx):
        await self._join(ctx)
        return

    @commands.command()
    async def play(self, ctx):
        await ctx.send("TODO")
        return

    async def _join(self, ctx):
        voice_client = await ctx.message.author.voice.channel.connect()
        return
