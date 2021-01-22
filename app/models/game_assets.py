from app.models.game import Game
from app.models.player import Player

players = []
game = Game()
acceptable_answers = []

def add_player(player):
    players.append(player)