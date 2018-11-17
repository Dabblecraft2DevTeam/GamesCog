import discord
import random
import time
from discord.ext import commands

class GamesCog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """This does stuff!"""
        #Your code will go here
	list = ["Do \help for help", "I am the walrus", "To kill a mocking bird", "Living is easy with eyes closed", "Misunderstanding all you see"]
	while True:
        	time.sleep(60)
		await client.change_presence(game=discord.Game(name=random.choice(list)))
		
def setup(bot):
    bot.add_cog(Mycog(bot))
