from src.probability.monte_carlo import estimate_win_prob

class LearningEVAgent:
    def __init__(self, name, pot=50, cost=25):
        self.name = name
        self.hand = []
        self.pot = pot
        self.cost = cost
        self.win_history = []
        self.threshold = 0  # initial EV threshold

    def decide(self, num_players):
        win_prob = estimate_win_prob(self.hand, num_players)
        ev = win_prob * self.pot - (1 - win_prob) * self.cost

        # Adjust decision threshold based on past performance
        if self.win_history:
            recent_win_rate = sum(self.win_history[-20:]) / min(len(self.win_history), 20)
            # If recent wins low → be more cautious
            self.threshold = max(0, ev * (0.5 + recent_win_rate/2))
        else:
            self.threshold = 0

        decision = "PLAY" if ev >= self.threshold else "FOLD"

        print(f"{self.name} hand: {self.hand}")
        print(f"Win probability: {win_prob:.3f}, EV: {ev:.2f}, Threshold: {self.threshold:.2f}")
        print(f"Decision: {decision}")

        return decision

    def record_result(self, won):
        # Record 1 for win, 0 for loss
        self.win_history.append(1 if won else 0)
