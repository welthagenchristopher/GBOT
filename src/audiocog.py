#audiocog.py

import asyncio
from pathlib import Path

import discord
from discord.ext import commands
from discord import FFmpegPCMAudio, PCMVolumeTransformer


class AudioCog(commands.Cog):
    def __init__(self, bot: commands.Bot, target_id: int):
        self.bot        = bot
        self.target_id  = target_id

        base_dir = Path(__file__).parent
        self.audio_path = str(base_dir / "audio.mp3")

        if not Path(self.audio_path).is_file():
            raise FileNotFoundError(f"Missing audio.mp3 at {self.audio_path}")
        
        self._task      = None

    @commands.Cog.listener()
    async def on_voice_state_update(self,
        member: discord.Member,
        before: discord.VoiceState,
        after: discord.VoiceState
    ):
        
        if member.id != self.target_id:
            return

        # when target join or switch into a channel
        if before.channel != after.channel and after.channel:
            # connect or move
            vc = member.guild.voice_client

            if vc and vc.is_connected():
                await vc.move_to(after.channel)

            else:
                vc = await after.channel.connect()

            # cancel any existing loop
            if self._task:
                self._task.cancel()

            # 2 second delay loop
            self._task = self.bot.loop.create_task(self._repeat_play(vc, delay=1))

        # target leaves, disconnect
        elif after.channel is None and before.channel:

            if self._task:
                self._task.cancel()
                self._task = None
            vc = member.guild.voice_client

            if vc and vc.is_connected():
                await vc.disconnect()

    async def _repeat_play(self, vc: discord.VoiceClient, delay: float):
        try:

            while vc.is_connected():
                # wait until not playing
                if not vc.is_playing():
                    # fresh instance per play
                    ff = FFmpegPCMAudio(self.audio_path, executable=<path_here_or_use_env>)
                    src = PCMVolumeTransformer(ff, volume=10)
                    vc.play(src, after=lambda e: print("playback err", e) if e else None)
                await asyncio.sleep(delay)

        except asyncio.CancelledError:
            # task cancelled (user left / moved), swallow it
            pass





