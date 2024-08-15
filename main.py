from time import sleep
import cards
import player
from game import Game

players = [
    player.Player("Beardy"),
    player.Player("Baldy"),
    player.Player("Ginger"),
    player.Player("Curly"),
]

development = cards.Card(
    name="Development",
    initial_carbon_cost=1,
    base_carbon_cost_per_round=1,
    carbon_cost_max_multiplier=2,
    acceptance_probability=1,
    disaster_probability=0,
    final_credit=1,
    symbol="🏠",
)

coal = cards.Card(
    name="Coal",
    initial_carbon_cost=1,
    base_carbon_cost_per_round=2,
    carbon_cost_max_multiplier=0,
    acceptance_probability=0.5,
    disaster_probability=0,
    final_credit=1,
    symbol="🏭",
)

forest = cards.Card(
    name="Forest",
    initial_carbon_cost=2,
    base_carbon_cost_per_round=-2,
    carbon_cost_max_multiplier=0,
    acceptance_probability=0.5,
    disaster_probability=0.1, #fires
    final_credit=2,
    symbol="🌲",
)

wind = cards.Card(
    name="Wind",
    initial_carbon_cost=2,
    base_carbon_cost_per_round=-1,
    carbon_cost_max_multiplier=6,
    acceptance_probability=0.5,
    disaster_probability=0,
    final_credit=2,
    symbol="🌬️",
)

solar = cards.Card(
    name="Solar",
    initial_carbon_cost=2,
    base_carbon_cost_per_round=-1,
    carbon_cost_max_multiplier=6,
    acceptance_probability=0.5,
    disaster_probability=0,
    final_credit=2,
    symbol="☀️",
)

nuclear = cards.Card(
    name="Nuclear",
    initial_carbon_cost=4,
    base_carbon_cost_per_round=-4,
    carbon_cost_max_multiplier=0,
    acceptance_probability=0.5,
    disaster_probability=0.1,
    final_credit=2,
    symbol="☢️",
)

game_cards = []
game_cards.extend([development] * 10)
game_cards.extend([coal] * 4)
game_cards.extend([forest] * 4)
game_cards.extend([wind] * 4)
game_cards.extend([solar] * 4)
game_cards.extend([nuclear] * 4)

print(f"Starting a game with {len(players)} players...")
g = Game(
    players=players,
    starting_carbon_credits=20,
    max_credits_lost_per_turn=6,
    game_cards=game_cards,
    target_card_count=5,
)

print("")
print("Cards in the deck:")
g.show_cards()

print("")
print("Players (carbon credit):")

g.status()

for i in range(20):
    print("----------------------------")
    print(f"\nRound {i + 1}:")
    sleep(1)
    g.next_round()
    g.status()
