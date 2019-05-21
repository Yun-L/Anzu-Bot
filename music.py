'''

Author: Yun

'''

import discord
import os
import asyncio
import queue

from discord.ext import commands
from urllib.parse import urlparse


class Song():

    def __init__(self, song, song_type, origin_ctx):
        self.song = song
        self.song_type = song_type
        self.origin_ctx = origin_ctx

    def entry_text(self):
        s = "Entry\n song: {}\n type: {}\n".format(self.song,
                                                   self.song_type)
        return s

    def finish_text(self):
        s = "Finished\n song: {}\n type: {}\n".format(self.song,
                                                      self.song_type)
        return s


class VoiceState():

    def __init__(self, bot, voice_client):
        self.bot = bot
        self.voice_client = voice_client
        self.song_list = queue.Queue()
        self.current_song = None

    async def _play_url(self, song_obj):

        await song_obj.origin_ctx.send(
            'this is a url: {}'.format(song_obj.song))

        return

    async def _play_local_file(self, song_obj):

        song_name = './songs/' + song_obj.song

        self.voice_client.play(discord.FFmpegPCMAudio(song_name),
                               after=self.after_song)

        return

    async def _play(self):

        self.current_song = self.song_list.queue[0]

        if self.current_song.song_type == 'local':
            await self._play_local_file(self.current_song)
        elif self.current_song.song_type == 'url':
            await self._play_url(self.current_song)
        else:
            return

    async def add_song(self, song_obj):
        await song_obj.origin_ctx.send(song_obj.entry_text())
        await song_obj.origin_ctx.send(self.song_list.queue)

        if self.song_list.empty():
            self.song_list.put(song_obj)
            await song_obj.origin_ctx.send("queue was empty")
            await self._play()
        else:
            self.song_list.put(song_obj)

        return

    def after_song(self, error):
        self.song_list.get()
        after_msg = self.current_song.origin_ctx.finish_text()
        send_msg_coro = self.current_song.origin_ctx.send(after_msg)
        play_next_coro = self._play()
        fut1 = asyncio.run_coroutine_threadsafe(send_msg_coro, self.bot.loop)
        fut2 = asyncio.run_coroutine_threadsafe(play_next_coro, self.bot.loop)
        try:
            fut1.result()
            fut2.rusult()
        except Exception as e:
            print('after_song failed: {}'.format(e))


class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        if not discord.opus.is_loaded():
            discord.opus.load_opus()
        self.voice_state = None

    # Private Methods

    def _get_local_songlist(self):
        song_list = os.listdir('./songs/')
        song_list.sort()
        song_list = '```' + '\n'.join(song_list) + '```'

        return song_list

    async def _join(self, ctx):

        author_voice_state = ctx.message.author.voice

        # Check if author is in a voice channel
        if author_voice_state is None:
            try:
                await ctx.send('You need to be in a voice channel' +
                               'for me to join')
            except discord.HTTPException:
                print('sending the message failed')
            finally:
                return

        # Create a new voicestate, or use existing one
        if self.voice_state is None:

            try:
                voice_client = await author_voice_state.channel.connect()
                self.voice_state = VoiceState(self.bot, voice_client)
            except Exception as e:
                print("failed create new voiceState: {}".format(e))

        elif self.voice_state.voice_client.is_connected():

            try:
                await self.voice_state.voice_client.move_to(
                    author_voice_state.channel)
            except Exception as e:
                print("failed move_to: {}".format(e))

        return

    async def _leave(self, ctx):

        print(self.voice_state)

        if self.voice_state is None:
            await ctx.send('I am not currently in a voice channel')

        else:
            await self.voice_state.voice_client.disconnect()
            self.voice_state = None

    # Bot Commands

    @commands.command()
    async def join(self, ctx):

        await self._join(ctx)

        return


    @commands.command()
    async def leave(self, ctx):

        await self._leave(ctx)

        return


    @commands.command()
    async def local_song_list(self, ctx):

        await ctx.send(self._get_local_songlist())

        return


    @commands.command()
    async def play(self, ctx, song_name):

        await self._join(ctx)

        # Check if song is a url

        url = urlparse(song_name)

        if url.netloc != '' or url.scheme != '':
            song = Song(url.geturl(), 'url', ctx)
            await self.voice_state.add_song(song)
            return

        # Check if song is a local file

        song_list = os.listdir('./songs/')

        if song_name in song_list:
            song = Song(song_name, 'local', ctx)
            await self.voice_state.add_song(song)
            return

        # Search youtube for possibilities

        await ctx.send("search for possibilities")
        return

    @commands.command()
    async def playl(self, ctx, song_name):
        song_list = self._get_local_songlist()

        if song_name not in song_list:
            await ctx.send('{} was not found')
            return

        await self._join(ctx)

        song_name = './songs/' + song_name

        self.voice_client.play(discord.FFmpegPCMAudio(song_name))

        return

    # @commands.command()
    # async def pause(self, ctx):
    #     if self.voice_client.is_playing():
    #         self.voice_client.pause()

    #     return

    # @commands.command()
    # async def resume(self, ctx):
    #     if self.voice_client.is_paused():
    #         self.voice_client.resume()

    #     return

    # @commands.command()
    # async def stop(self, ctx):
    #     self.voice_client.stop()

    #     return


def setup(bot):
    bot.add_cog(Music(bot))
