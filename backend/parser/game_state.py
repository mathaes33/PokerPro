class Player:
    def __init__(self, name, stack):
        self.name = name
        self.stack = stack

class GameState:
    def __init__(self):
        self.players = []
        self.pot = 0.0
