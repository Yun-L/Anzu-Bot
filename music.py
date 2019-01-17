import discord, asyncio
from discord.ext import commands

class SongObj:
    def __init__(self, requester, song):
        self.song = song
        self.requester = requester


class State:
    def __init__(self, bot):
        self.serverID = ''
        self.songs = asyncio.Queue()
        self.voice_client = None


class Music:
    def __init__(self, bot):
        self.bot = bot
        self.states = {}


    @command.commands(pass_context = True)
    async def join(ctx):
        pass


def setup(bot):
    bot.add_cog(Music(bot))
