import discord
import random
import time
from discord.ext import commands

class GamesCog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
    @bot.event()
    async def change_status(self):
        l = ["Do \help for help", "I am the walrus", "To kill a mocking bird", "Living is easy with eyes closed, Misunderstanding all you see"]
        await self.change_presence(activity=discord.Game(name=random.choice(l)))
        await asyncio.sleep(60)


    async def on_ready(self):
        print(f'Username: {self.user.name}')
        print(f'Client ID: {self.user.id}')
        self.bg_task = self.loop.create_task(self.change_status())
def setup(bot):
    bot.add_cog(GamesCog(bot))
