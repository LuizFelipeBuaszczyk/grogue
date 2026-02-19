
class UserAlreadyResponded(Exception):
    def __init__(self):
        self.message = "O usuário ja fez uma jogada!"

class ChallangeNotExists(Exception):
    def __init__(self):
        self.message = "O desafio nao existe!"

class UsersAreSame(Exception):
    def __init__(self):
        self.message = "Os usuários nao podem ser iguais!"
