import random

class RandomAgent:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def decide(self, num_players, pot=50, cost=25):
        decision = random.choice(["PLAY", "FOLD"])
        print(f"{self.name} hand: {self.hand}")
        print(f"Decision: {decision}")
        return decision
