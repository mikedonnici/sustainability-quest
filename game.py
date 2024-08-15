from time import sleep

import player
import random
from cards import Card


class Game:

    def __init__(self, players: list, starting_carbon_credits: int, max_credits_lost_per_turn, game_cards: list[Card], target_card_count):
        self.players = players
        self.cards = game_cards
        self.shuffle_cards()
        self.round = 0
        self.next_player_index = 0
        self.target_card_count = target_card_count
        self.max_credits_lost_per_turn = max_credits_lost_per_turn

        for p in self.players:
            p.carbon_credits = starting_carbon_credits

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def show_cards(self):
        """Prints the cards in the deck"""
        for card in self.cards:
            print(f"{card.show()}", end="\t", flush=True)

    def status(self):
        """prints each player and their current carbon_credits"""
        for p in self.players:
            print(f"{p.name}\t{p.all_cards_str()}\t{p.carbon_credits} carbon credits")

    def next_round(self):
        """Simulates the next round in the game"""
        # if all players have reached the target card count, the game is over
        if self.game_over():
            w = self.winner()
            print(f"All players have {self.target_card_count} cards - game over!")
            print(f"{w.name} wins with {w.final_score()} carbon credits")
            exit(0)

        for p in self.players:
            p.take_turn(self)

    def game_over(self):
        """Returns True if all players have reached the target card count"""
        for p in self.players:
            if len(p.cards) < self.target_card_count:
                return False
        return True

    def winner(self):
        """Returns the player with the most carbon credits"""
        winner = max(self.players, key=lambda x: x.final_score())
        return winner
