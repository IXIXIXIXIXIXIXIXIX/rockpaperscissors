class Player:

    def __init__(self, name):
        self.name = name
        self.choice = None
        self.score = 0

    def choose(self, choice):
        self.choice = choice

    def reset(self):
        self.choice = None

    def increase_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0