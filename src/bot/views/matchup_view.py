import discord

class MatchupView(discord.ui.View):

    @discord.ui.button(label='Aceitar')
    async def button_accept(self, interact: discord.Interaction, button: discord.ui.Button):
        await interact.response.send_message(f"O usuário {interact.user.name} aceitou o desafio!")
    
    @discord.ui.button(label='Rejeitar')
    async def button_reject(self, interact: discord.Interaction, button: discord.ui.Button):
        await interact.response.send_message(f"O usuário {interact.user.name} rejeitou o desafio!")