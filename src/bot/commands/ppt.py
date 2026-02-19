import discord
from discord.ext import commands
from bot.views.ppt_view import PptView

from bot.services.ppt_service import PptService

def setup(bot: commands.Bot):

    @bot.tree.command()
    async def ppt(interect: discord.Interaction, challenged: discord.Member):
        await interect.response.defer()

        if interect.user.id == challenged.id:
            await interect.followup.send("Os usuários nao podem ser iguais!", ephemeral=True)
            return       
        
        embed = discord.Embed(
            title=f"Pedra, Papel ou Tesoura",
            description=f"O usuário {interect.user.mention} desafiou {challenged.mention}!"
        )
        
        send_message: discord.webhook.WebhookMessage = await interect.followup.send(
            embed=embed,
            view=PptView()
        )

        PptService.post_challange(
            id_message=send_message.id,
            user1=interect.user,
            user2=challenged
        )

        