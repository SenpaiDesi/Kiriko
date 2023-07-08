import datetime
import discord
from discord.app_commands import Choice
from discord import app_commands
from discord.ext import commands
import time
import platform
import asyncio
import utils as utilities
from utils import logname
current_uptime = time.time()


class sfx(commands.Cog):
    """Some funny vc commands"""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    

    @app_commands.command(name="sfx", description="Play some kiriko sound effects. YIP YIP!")
    @utilities.check_blacklist()
    @app_commands.describe(line = "The voiceline you want to play")
    @app_commands.choices(line = [
        Choice(name="bai bai", value="baibai"),
        Choice(name="Wait till you see me on my bike", value="bike"),
        Choice(name="I run with blades", value="blades"),
        Choice(name="Yip Yip!", value="yip"),
        Choice(name="Aw yeah", value="awyeah"),
        Choice(name="Nah", value="nah"),
        Choice(name="Hi", value="hi"),
        Choice(name="The weak are food for the strong", value="theweak"),
        Choice(name="That is fox power", value="foxpower"),
        Choice(name="So long bestie", value="bestie"),
        Choice(name="Some of the old, some of the new", value="someoldsomenew"),
        Choice(name="Push a rock", value="rock"),
        Choice(name="Lonely in here", value="lonely"),
        Choice(name="Keep calm, Keep sly", value="sly"),
        Choice(name="Hey Queen", value="queen"),
        Choice(name="Laughing", value="laugh")
    ])
    async def playsfx(self, interaction : discord.Interaction, line:str):
        channel = interaction.user.voice.channel
        try:
            vc = await channel.connect()
        except discord.ClientException:
            return await interaction.response.send_message(f"Sorry I am already playing in another channel. That channel being {channel.mention}", ephemeral=True)
        source= discord.FFmpegPCMAudio(source= f"/root/Kiriko/fun/sfx/{line}.ogg")
        await interaction.response.send_message(f"Okay, Playing in {channel.mention}", ephemeral=True)
        vc.play(source)
        while vc.is_playing():
            await asyncio.sleep(.1)
        await vc.disconnect()



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(sfx(bot))