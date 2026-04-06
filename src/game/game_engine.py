from src.game.deck import Deck
from src.probability.hand_evaluator import evaluate_hand

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

class GameEngine:
    def __init__(self, num_players):
        self.players = [Player(f"P{i}") for i in range(num_players)]
        self.deck = Deck()

    def deal_cards(self):
        self.deck.shuffle()
        for player in self.players:
            player.hand = self.deck.deal(3)

    def resolve_winner(self):
        best_score = None
        winner = None

        for player in self.players:
            score = evaluate_hand(player.hand)

            if best_score is None or score > best_score:
                best_score = score
                winner = player

        return winner

    def play_game(self):
        self.deal_cards()

        for p in self.players:
            print(p.name, p.hand)

        winner = self.resolve_winner()
        print("Winner:", winner.name)
