from discord.ext import commands

def init(bot: commands.Bot):

    @bot.event
    async def on_ready():
        await bot.tree.sync()