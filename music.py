'''

Author: Yun

'''

import discord
from discord.ext import commands


class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.voice_client = None
        if not discord.opus.is_loaded():
            discord.opus.load_opus()

    @commands.command()
    async def join(self, ctx):

        author_voice_state = ctx.message.author.voice

        # Check if author is in a voice channel
        if not author_voice_state:
            try:
                await ctx.send('You need to be in a voice channel' +
                               'for me to join')
            except discord.HTTPException:
                print('sending the message failed')
            finally:
                return

        # Join channel, ClientException raises when bot is already in a channel
        try:
            self.voice_client = await author_voice_state.channel.connect()
        except discord.ClientException:
            await self.voice_client.move_to(author_voice_state.channel)
        except Exception as e:
            print(e)
            raise
        finally:
            return

    @commands.command()
    async def leave(self, ctx):

        if self.voice_client is not None:
            await self.voice_client.disconnect()
            self.voice_client = None
        else:
            await ctx.send('I am not in a currently voice channel')
        return


def setup(bot):
    bot.add_cog(Music(bot))
