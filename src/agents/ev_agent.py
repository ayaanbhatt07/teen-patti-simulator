from src.probability.monte_carlo import estimate_win_prob


class EVAgent:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def decide(self, num_players, pot=50, cost=25):
        win_prob = estimate_win_prob(self.hand, num_players)

        ev = win_prob * pot - (1 - win_prob) * cost

        print(f"{self.name} hand: {self.hand}")
        print(f"Win probability: {win_prob:.2f}")
        print(f"EV: {ev:.3f}")

        if ev > 0:
            return "PLAY"
        else:
            return "FOLD"

