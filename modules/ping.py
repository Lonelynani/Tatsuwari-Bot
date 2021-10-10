import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.command_name = "ping"

    @commands.command()
    async def ping(self,ctx):
        await ctx.send("Ping!")

def setup(bot):
    bot.add_cog(Ping(bot))
    print(f"Loaded: {Ping(bot).command_name}")