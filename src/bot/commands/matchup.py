import discord
from discord.ext import commands

def setup(bot: commands.Bot):

    @bot.command()
    async def matchup(ctx: commands.Context, challenged: discord.Member):
        embed = discord.Embed(
            title=f"{ctx.author.name} vs {challenged.name}",
            color=discord.Color.from_rgb(255, 0, 0),
            description=f"O usuário {ctx.author.mention} desafiou o usuário {challenged.mention}!"
        )
        await ctx.send(
            embed=embed
        )