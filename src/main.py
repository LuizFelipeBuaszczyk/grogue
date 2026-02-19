import os
from dotenv import load_dotenv
from bot.Grogue import Grogue

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Grogue(BOT_TOKEN)

bot.run()