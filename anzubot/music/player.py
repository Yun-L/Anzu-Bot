import discord
from discord.ext import commands


class Player():
    """
    Describes a single player for a guild.
    """

    def __init__(self, bot: commands.Bot, voice_client: discord.VoiceClient):
        self.bot = bot
        self.voice_client = voice_client
