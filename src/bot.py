# bot.py

from discord.ext import commands

from src.audiocog import AudioCog

class TheBot(commands.Bot):
    def __init__(self, token: str, target_id: int, **options):
        self._token      = token
        self._target_id  = target_id
        super().__init__(**options)

    async def setup_hook(self):
        # this is run *before* the bot logs in
        await self.add_cog(AudioCog(self, self._target_id))
        print(f"✅ AudioCog loaded for user {self._target_id}")
