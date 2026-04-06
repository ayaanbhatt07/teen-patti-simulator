from src.game.deck import Deck
from src.agents.ev_agent import EVAgent
from src.agents.random_agent import RandomAgent
from src.probability.monte_carlo import estimate_win_prob

def run_simulation(num_games=1000):
    ev_wins = 0
    random_wins = 0

    for game in range(num_games):
        deck = Deck()
        deck.shuffle()

        # Create agents
        ev_agent = EVAgent("EV_Player")
        random_agent = RandomAgent("Random_Player")

        # Deal hands
        ev_agent.hand = deck.deal(3)
        random_agent.hand = deck.deal(3)

        # Decide actions
        ev_decision = ev_agent.decide(num_players=2, pot=50, cost=25)
        random_decision = random_agent.decide(num_players=2, pot=50, cost=25)

        # Determine winner among PLAYERS only
        # Simple rule: highest hand among PLAY decisions wins
        candidates = []
        if ev_decision == "PLAY":
            candidates.append(("EV_Player", ev_agent.hand))
        if random_decision == "PLAY":
            candidates.append(("Random_Player", random_agent.hand))

        if not candidates:
            continue  # everyone folded → skip game

        winner = max(candidates, key=lambda x: estimate_win_prob(x[1], num_players=2, simulations=500))
        if winner[0] == "EV_Player":
            ev_wins += 1
        else:
            random_wins += 1

    print(f"EV Agent win rate: {ev_wins / num_games:.2%}")
    print(f"Random Agent win rate: {random_wins / num_games:.2%}")
