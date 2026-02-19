from discord.user import User
from bot.exceptions.exceptions import UserAlreadyResponded, ChallengeNotExists, UsersAreSame, UserIsntInChallange

from bot.enums.status_game_enum import StatusGame

RESPONSES = {}

class PptService:

    @staticmethod
    def post_challange(id_message: str, user1: User, user2: User):
        if user1.id == user2.id:
            raise UsersAreSame
        
        RESPONSES[id_message] = {
            user1.id: None,
            user2.id: None,
            
        }
        return

    @staticmethod
    def post_response(response: str, user: User, id_message: str):
        data = {
            "response": response,
            "user": user
        }

        challenge: dict = RESPONSES.get(id_message)
        if not challenge:
            raise ChallengeNotExists

        if challenge.get(user.id):
            raise UserAlreadyResponded
        
        if user.id not in challenge.keys():
            raise UserIsntInChallange
        
        challenge[user.id] = data
        RESPONSES[id_message] = challenge

        return
    
    @staticmethod
    def verify_response(id_message: str)-> dict:

        challenge: dict = RESPONSES.get(id_message)
        
        if not challenge:
            raise ChallengeNotExists
        

        keys = list(challenge.keys())
        
        res = {
            "winner": None,
            "status": StatusGame.WAITING
        }
        
        
        responses = [challenge[key] for key in keys if challenge[key]]
        if len(responses) < 2:
            return res
        
        res["status"] = StatusGame.FINISHED
        RESPONSES[id_message] = None

        if responses[0]["response"] == responses[1]["response"]:
            return res

        if responses[0]["response"] == "pedra":
            if responses[1]["response"] == "tesoura":
                res["winner"] = responses[0]["user"]
            else:
                res["winner"] = responses[1]["user"]
        elif responses[0]["response"] == "papel":
            if responses[1]["response"] == "pedra":
                res["winner"] = responses[0]["user"]
            else:
                res["winner"] = responses[1]["user"]
        else:
            if responses[1]["response"] == "papel":
                res["winner"] = responses[0]["user"]
            else:
                res["winner"] = responses[1]["user"]

        return res