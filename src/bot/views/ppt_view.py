import discord

from bot.services.ppt_service import PptService
from bot.enums.ppt_enum import Ppt
from bot.enums.status_game_enum  import StatusGame

from bot.exceptions.exceptions import UserAlreadyResponded, ChallengeNotExists, UserIsntInChallange

class PptView(discord.ui.View):

    options = [
        discord.SelectOption(label=Ppt.PAPER.value),
        discord.SelectOption(label=Ppt.ROCK.value),
        discord.SelectOption(label=Ppt.SCISSORS.value)
    ]

    @discord.ui.select(placeholder="Pedra, Papel ou Tesoura", options=options)
    async def select_response(self, interact: discord.Interaction, select: discord.ui.Select):
        try:
            PptService.post_response(response=select.values[0], 
                                    user=interact.user,
                                    id_message=interact.message.id)
            await interact.response.send_message(f"O usuário {interact.user.name} realizou a jogada.")
        except UserAlreadyResponded:
            await interact.response.send_message(f"A sua jogada já foi efetuada anteriormente, não é posível muda-lá.", ephemeral=True)
            return
        except ChallengeNotExists:
            await interact.response.send_message(f"O desafio nao existe!", ephemeral=True)
            return
        except UserIsntInChallange:
            await interact.response.send_message(f"Você não faz parte deste desafio.", ephemeral=True)
            return
        try:
            winner = PptService.verify_response(id_message=interact.message.id)
            
            if winner["status"] == StatusGame.FINISHED:
                if winner["winner"]:
                    await interact.followup.send(f"O jogo acabou! O ganhador foi: {winner['winner'].name}")
                else:
                    await interact.followup.send("O jogo acabou em empate!")
        except ChallengeNotExists:
            await interact.followup.send(f"O desafio nao existe!", ephemeral=True)
            return