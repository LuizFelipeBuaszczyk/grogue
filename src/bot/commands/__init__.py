from discord.ext.commands import Bot 

def init(bot: Bot):
    from . import matchup
    from . import ppt


    matchup.setup(bot)
    ppt.setup(bot)

