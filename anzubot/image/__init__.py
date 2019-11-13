from .image import Image

# Image extensions entry point


def setup(bot):
    bot.add_cog(Image(bot))
