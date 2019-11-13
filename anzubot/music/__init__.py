import discord.opus as opus

from .music import Music

# Music extensions entry point


def setup(bot):
    bot.add_cog(Music(bot))

# Potentially load opus library if voice doesn't work
