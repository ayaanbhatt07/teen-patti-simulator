import random
from src.game.deck import Deck
from src.probability.hand_evaluator import evaluate_hand


def estimate_win_prob(my_hand, num_players, simulations=2000):
    wins = 0

    for _ in range(simulations):
        deck = Deck()
        deck.cards = [c for c in deck.cards if c not in my_hand]

        random.shuffle(deck.cards)

        opponent_hands = []

        # deal to opponents
        for _ in range(num_players - 1):
            opponent_hands.append([deck.cards.pop(), deck.cards.pop(), deck.cards.pop()])

        my_score = evaluate_hand(my_hand)

        win = True
        for opp in opponent_hands:
            if evaluate_hand(opp) > my_score:
                win = False
                break

        if win:
            wins += 1

    return wins / simulations
