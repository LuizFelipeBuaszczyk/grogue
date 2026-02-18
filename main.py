import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

# Inicializando o bot com todas as permissões
intents = discord.Intents.all()

bot = commands.Bot(".", intents=intents)

bot.run(BOT_TOKEN)