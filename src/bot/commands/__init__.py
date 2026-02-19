from discord.ext.commands import Bot 

def init(bot: Bot):
    from . import matchup


    matchup.setup(bot)

