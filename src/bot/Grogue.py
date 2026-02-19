import discord
import bot.commands as cmd
import bot.events as evt

from discord.ext import commands

class Grogue:
    
    def __init__(self, bot_token:str):
        # Inicializando o bot com todas as permissões
        self.intents = discord.Intents.all()
        self.bot = commands.Bot(".", intents=self.intents)
        self.token = bot_token
        self.__load_events()
        self.__load_commands()

    def __load_events(self):
        evt.init(self.bot)

    def __load_commands(self):
        cmd.init(self.bot)

    def run(self):
        self.bot.run(self.token)
