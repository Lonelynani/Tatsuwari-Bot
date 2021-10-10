import discord
from discord.ext import commands
from requests_html import HTML,HTMLSession
class Search(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.command_name = "Search"

    @commands.command()
    async def search(self,ctx,word):
        session = HTMLSession()
        if " " in word: str(word).replace("+")

        r = session.get(f"https://www.google.com/search?client=firefox-b-1-d&q=definition+search#dobs={word}")

        html = HTML(html=r.text)
        i = html.find(".eQJLDd")
        await ctx.send(i[0].text)

        pass

def setup(bot):
    bot.add_cog(Search(bot))
    print(f"Loaded: {Search(bot).command_name}")