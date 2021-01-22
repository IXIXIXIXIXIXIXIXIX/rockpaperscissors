import unittest
from app.models.game import Game 
from app.models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):

        self.player1 = Player("Player1")
        self.player2 = Player("Player2")
        self.game = Game()

    # Test outcomes if somehow neither or both players choose yet the game still runs
    def test_neither_choose(self):

        self.assertEqual(None, self.game.play(self.player1, self.player2))
        self.assertEqual(0, self.player1.score)
        self.assertEqual(0, self.player2.score)

    def test_player1_does_not_choose(self):
        self.player2.choose("Paper")

        self.assertEqual(self.player2, self.game.play(self.player1, self.player2))
        self.assertEqual(1, self.player2.score)
        self.assertEqual(0, self.player1.score)

    def test_player2_does_not_choose(self):
        self.player1.choose("Rock")

        self.assertEqual(self.player1, self.game.play(self.player1, self.player2))
        self.assertEqual(1, self.player1.score)
        self.assertEqual(0, self.player2.score)

    # Test all valid outcomes in base game
    def test_R_R(self):
        self.player1.choose("Rock")
        self.player2.choose("Rock")

        self.assertEqual(None, self.game.play(self.player1, self.player2))
        self.assertEqual(0, self.player1.score)
        self.assertEqual(0, self.player2.score)

    def test_R_P(self):
        self.player1.choose("Rock")
        self.player2.choose("Paper")

        self.assertEqual(self.player2, self.game.play(self.player1, self.player2))
        self.assertEqual(1, self.player2.score)
        self.assertEqual(0, self.player1.score)

    def test_R_S(self):
        self.player1.choose("Rock")
        self.player2.choose("Scissors")

        self.assertEqual(self.player1, self.game.play(self.player1, self.player2))
        self.assertEqual(1, self.player1.score)
        self.assertEqual(0, self.player2.score)

    def test_P_R(self):
        self.player1.choose("Paper")
        self.player2.choose("Rock")

        self.assertEqual(self.player1, self.game.play(self.player1, self.player2))
        self.assertEqual(1, self.player1.score)
        self.assertEqual(0, self.player2.score)

    def test_P_P(self):
        self.player1.choose("Paper")
        self.player2.choose("Paper")

        self.assertEqual(None, self.game.play(self.player1, self.player2))
        self.assertEqual(0, self.player1.score)
        self.assertEqual(0, self.player2.score)

    def test_P_S(self):
        self.player1.choose("Paper")
        self.player2.choose("Scissors")

        self.assertEqual(self.player2, self.game.play(self.player1, self.player2))
        self.assertEqual(1, self.player2.score)
        self.assertEqual(0, self.player1.score)

    def test_S_R(self):
        self.player1.choose("Scissors")
        self.player2.choose("Rock")

        self.assertEqual(self.player2, self.game.play(self.player1, self.player2))
        self.assertEqual(1, self.player2.score)
        self.assertEqual(0, self.player1.score)

    def test_S_P(self):
        self.player1.choose("Scissors")
        self.player2.choose("Paper")

        self.assertEqual(self.player1, self.game.play(self.player1, self.player2))
        self.assertEqual(1, self.player1.score)
        self.assertEqual(0, self.player2.score)

    def test_S_S(self):
        self.player1.choose("Scissors")
        self.player2.choose("Scissors")

        self.assertEqual(None, self.game.play(self.player1, self.player2))
        self.assertEqual(0, self.player1.score)
        self.assertEqual(0, self.player2.score)

    # Testing extended game - only need to test all of the potential P2 losers for one given P1 winner
    def test_spock_scissors(self):
        self.player1.choose("Spock")
        self.player2.choose("Scissors")

        self.assertEqual(self.player1, self.game.play(self.player1, self.player2))
        self.assertEqual(1, self.player1.score)
        self.assertEqual(0, self.player2.score)
    
    def test_spock_rock(self):
        self.player1.choose("Spock")
        self.player2.choose("Rock")

        self.assertEqual(self.player1, self.game.play(self.player1, self.player2))
        self.assertEqual(1, self.player1.score)
        self.assertEqual(0, self.player2.score)