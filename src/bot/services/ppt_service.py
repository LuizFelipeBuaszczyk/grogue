from discord.user import User
from bot.exceptions.exceptions import UserAlreadyResponded, ChallangeNotExists, UsersAreSame

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

        challange: dict = RESPONSES.get(id_message)
        if not challange:
            raise ChallangeNotExists

        if challange.get(user.id):
            raise UserAlreadyResponded
        
        challange[user.id] = data
        RESPONSES[id_message] = challange

        return
    
    @staticmethod
    def verify_response(id_message: str):

        challange: dict = RESPONSES.get(id_message)

        if not challange:
            raise ChallangeNotExists
        

        keys = list(challange.keys())
        
        res = {
            "winner": None,
            "status": StatusGame.WAITING
        }
        
        
        responses = [challange[key] for key in keys if challange[key]]
        if len(responses) < 2:
            return res
        
        res["status"] = StatusGame.FINISHED

        if responses[0]["response"] == responses[1]["response"]:
            return 

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