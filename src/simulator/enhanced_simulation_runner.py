import csv
import matplotlib.pyplot as plt
from src.game.deck import Deck
from src.agents.learning_ev_agent import LearningEVAgent
from src.agents.random_agent import RandomAgent
from src.probability.monte_carlo import estimate_win_prob

def run_enhanced_simulation(num_games=500, verbose=False):
    ev_wins = 0
    random_wins = 0

    # Keep history for plotting
    ev_history = []
    random_history = []

    for game in range(1, num_games + 1):
        deck = Deck()
        deck.shuffle()

        # Create agents
        ev_agent = LearningEVAgent("LearningEV_Player")
        random_agent = RandomAgent("Random_Player")

        # Deal hands
        ev_agent.hand = deck.deal(3)
        random_agent.hand = deck.deal(3)

        # Decide actions
        ev_decision = ev_agent.decide(num_players=2)
        random_decision = random_agent.decide(num_players=2)

        # Determine winner among PLAYERS only
        candidates = []
        if ev_decision == "PLAY":
            candidates.append(("LearningEV_Player", ev_agent.hand))
        if random_decision == "PLAY":
            candidates.append(("Random_Player", random_agent.hand))

        if not candidates:
            if verbose:
                print(f"Game {game}: all folded, skipping")
            continue  # everyone folded → skip game

        # Determine winner based on estimated win probability
        winner = max(candidates, key=lambda x: estimate_win_prob(x[1], num_players=2, simulations=500))

        if winner[0] == "LearningEV_Player":
            ev_wins += 1
            ev_agent.record_result(True)
        else:
            random_wins += 1
            ev_agent.record_result(False)

        # Save running win rate
        ev_history.append(ev_wins / game)
        random_history.append(random_wins / game)

        if verbose:
            print(f"Game {game} winner: {winner[0]}")

    # Save CSV
    with open("simulation_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Game", "EV_WinRate", "Random_WinRate"])
        for i in range(len(ev_history)):
            writer.writerow([i + 1, ev_history[i], random_history[i]])

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(ev_history) + 1), ev_history, label="LearningEV Agent", color="blue")
    plt.plot(range(1, len(random_history) + 1), random_history, label="Random Agent", color="red")
    plt.xlabel("Game")
    plt.ylabel("Cumulative Win Rate")
    plt.title("Teen Patti Strategy Simulation")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("win_rate_plot.png")  # save plot for GitHub
    plt.show()

    print(f"Final LearningEV Agent win rate: {ev_wins / num_games:.2%}")
    print(f"Final Random Agent win rate: {random_wins / num_games:.2%}")
