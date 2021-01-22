import unittest
from app.models.player import Player
from app.models.game import Game

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Player 1")

    def test_player_has_name(self):
        self.assertEqual("Player 1", self.player.name)

    def test_player_has_not_chosen(self):
        self.assertEqual(None, self.player.choice)

    def test_player_score_is_zero(self):
        self.assertEqual(0, self.player.score)

    def test_player_can_score(self):
        self.player.increase_score()
        self.assertEqual(1, self.player.score)

    def test_player_can_reset_score(self):
        self.player.increase_score()
        self.player.reset_score()
        
        self.assertEqual(0, self.player.score)

    def test_player_can_choose(self):
        self.player.choose("Rock")
        self.assertEqual("Rock", self.player.choice)

    def test_player_can_reset_choice(self):
        self.player.choose("Rock")
        self.assertEqual("Rock", self.player.choice)
        self.player.reset()
        self.assertEqual(None, self.player.choice)