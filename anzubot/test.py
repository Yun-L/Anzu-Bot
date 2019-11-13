import discord
from discord.ext import commands


class Test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        aliases=["ar", "ask"],
        brief="Test command/response")
    async def ask_response(self, ctx):
        await ctx.send(f"Responding to {ctx.author.display_name}")
        return

    @commands.command(
        brief="demonstrate markdown escape",
        aliases=["esc"])
    async def md_escape(self, ctx):
        await ctx.send("Non-escaped text: _aoeu_ ||aoeuaoeu||")
        esc = discord.utils.escape_markdown("Escaped: _aoeu_ ||aoeuaoeu||")
        await ctx.send(esc)
        return

    @commands.command(
        brief="demonstrate exception handling",
        aliases=["raise"])
    async def raise_exception(self, ctx):
        raise Exception("exception raised")

# Extension entry point


def setup(bot):
    bot.add_cog(Test(bot))
