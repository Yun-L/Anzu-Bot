import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

class SongObj_ytdl:
    def __init__(self, message, song_player):
        self.message = message
        self.song_player = song_player

    def __str__(self):
        return "playing song from SongObj_ytdl"

class SongObj_local:
    def __init(self, message, song_player):
        self.message = message
        self.song_player = song_player

    def __str__(self):
        return "playing song from SongObj_local"

class State:
    def __init__(self, bot):
        self.serverID = ''
        self.current = None
        self.songs = asyncio.Queue(maxsize=-1)
        self.start_next_song = asyncio.Event()
        self.voice_client = None


    def song_player(self):
        while True:
            self.start_next_song.clear()
            self.current = await self.songs.get()
            await self.current.song_player.start()
            await self.start_next_song.wait()


class Music:
    def __init__(self, bot):
        self.bot = bot
        self.voice_clients = {}

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state

        return state

    @commands.command(pass_context = True)
    async def play(self, ctx):
        await self.join(ctx)
        


    @commands.command(pass_context = True)
    async def join(self, ctx):
        try:
            channel = ctx.message.author.voice.voice_channel
            await self.bot.join_voice_channel(channel)

        except:
            await self.bot.say("You need to be in a voice channel for me to join.")


    @commands.command(pass_context = True)
    async def leave(self, ctx):
        server = ctx.message.server
        voice_client = self.bot.voice_client_in(server)
        await voice_client.disconnect()

    @commands.command(pass_context = True)
    async def playT(self, ctx):
        
        
        try:
            channel = ctx.message.author.voice.voice_channel
            await self.bot.join_voice_channel(channel)

        except:
            await self.bot.say("You need to be in a voice channel for me to join.")

        server = ctx.message.server
        voice_client = self.bot.voice_client_in(server)
        player = voice_client.create_ffmpeg_player("./songs/test.mp3")
        player.start()


    @commands.command(pass_context = True)
    async def testp(self, ctx, arg1, arg2):
        await self.bot.say("{}".format(ctx.message.content))
        await self.bot.say("r: [{}],[{}]".format(arg1, arg2))

    @commands.command(pass_context = True)
    async def db(self, ctx):
        await self.bot.say("server id: [{}]".format(ctx.message.server.id))
        await self.bot.say("author: [{}]".format(ctx.message.author))
        await self.bot.say(str(ctx))
        
def setup(bot):
    bot.add_cog(Music(bot))
