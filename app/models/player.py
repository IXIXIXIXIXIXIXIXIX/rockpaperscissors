import random

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


class Robot(Player):

    def __init__(self, name, answers):
        self.name = name
        self.answers = answers

        self.choice = None
        self.score = 0

    def choose(self):
        # self.choice = "Rock"
        self.choice = random.choice(self.answers)

    def reset(self):
        super().reset()

    def increase_score(self):
        super().increase_score()

    def reset_score(self):
        super().reset_score()