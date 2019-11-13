import discord
import configparser
import asyncio
from discord.ext import commands


config = configparser.ConfigParser()
config.read('config.ini')

PREFIX = config['Default']['Prefix']
TOKEN = config['Default']['Token']

extensions = ["test", "music"]


class AnzuBot(commands.Bot):

    def __init__(self, cmd_prefix):
        super(AnzuBot, self).__init__(command_prefix=cmd_prefix)

    # Overloading commands.Bot functions

    async def on_ready(self):
        await self.change_presence(activity=discord.Game(name="ee"))
        print("-"*20)
        print("Logged in as:")
        print(self.user.name)
        print(self.user.id)
        print(f"With bot prefix: {PREFIX}")
        print("-"*20)
        # TODO move output to logging
        return

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            error_msg = await ctx.send(
                f"'{ctx.message.content}' is not a valid command.\n "
                f"type {self.command_prefix}help for a list of commands."
            )

            await error_msg.delete(delay=5)
        else:
            print(f"Error: '{error}', triggered by "
                  f"command '{ctx.message.content}'")
        # TODO move output to logging
        return

    async def on_command(self, ctx):
        print(f"Command Found: '{ctx.message.content}'")
        # TODO move output to logging
        return

    async def on_command_completion(self, ctx):
        print(f"Finished: '{ctx.message.content}'")
        # TODO move output to logging
        return


if __name__ == "__main__":

    bot = AnzuBot(PREFIX)

    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"{extension} could not be loaded: {e}")

    bot.run(TOKEN)
