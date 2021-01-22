class Game:

    def __init__(self):

        self.beats = {
            "Rock": ["Scissors", "Lizard"],
            "Paper": ["Rock", "Spock"],
            "Scissors": ["Paper", "Lizard"],
            "Lizard": ["Spock", "Paper"],
            "Spock": ["Scissors", "Rock"]
        }


    def play(self, player1, player2):

        # Deal with all draw conditions
        if player1.choice == player2.choice:
            return None

        # Deal with either player somehow not choosing
        if player1.choice == None:
            player2.increase_score()
            return player2

        if player2.choice == None:
            player1.increase_score()
            return player1

        # Check if player2 loses and return accordingly
        if player2.choice in self.beats[player1.choice]:

            player1.increase_score()
            return player1

        else:
            player2.increase_score()
            return player2
