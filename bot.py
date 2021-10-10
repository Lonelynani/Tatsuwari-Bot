import discord
from discord.ext import commands
import os,json,random,time


config = json.load(open("config.json","r"))
bot = commands.Bot(command_prefix=config[0]["system_config"]["prefix"])

modules = [bot.load_extension(f"modules.{i.replace('.py','')}") for i in os.listdir("./modules/") if i.endswith(".py")] #Loads module from start
print(modules)
@bot.command()
async def load(ctx,file):
    try:
        bot.load_extension(f"modules.{file}")
    except Exception:
        await ctx.send(f"{file} doesn't exist or not found!")

@bot.command()
async def unload(ctx,file):
    try:
        bot.unload_extension(f"modules.{file}")
    except Exception:
        await ctx.send(f"{file} doesn't exist or not found!")

@bot.command()
async def reload(ctx,file):
    try:
        bot.reload_extension(f"modules.{file}")
    except Exception:
        await ctx.send(f"{file} doesn't exist or not found!")

bot.run(config[0]["system_config"]["token"])