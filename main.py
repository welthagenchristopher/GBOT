#main.py

import os
from pathlib import Path
import sys

from dotenv import load_dotenv
import discord

# generate path to bot class
sys.path.insert(0, str(Path(__file__).parent / "src"))
from src.bot import TheBot


def main():
    load_dotenv()  # reads .env in project root
    TOKEN     = os.getenv("DISCORD_TOKEN")
    TARGET_ID = int(os.getenv("TARGET_USER_ID"))

    intents = discord.Intents.default()
    intents.members = True
    intents.voice_states = True

    bot = TheBot(
        token=TOKEN,
        target_id=TARGET_ID,
        command_prefix="&",
        intents=intents,
        help_command=None,
    )
    bot.run(bot._token)

if __name__ == "__main__":
    main()
