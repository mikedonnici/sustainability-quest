import math

import dice
from cards import Card
from game import Game


class Player:

    def __init__(self, name: str):
        self.name = name
        self.carbon_credits = 0
        self.cards = []

    def __str__(self):
        return f"{self.name} has {self.carbon_credits} carbon credits"

    def add_card(self, card: Card):
        self.cards.append(card)

    def cards(self):
        for card in self.cards:
            print(card)

    def take_turn(self, game: Game):
        print(f"{self.name} takes a turn: ")
        self.possible_nuclear_meltdown()

        # only draw a new card if the player has less than game card target
        if len(self.cards) < game.target_card_count:
            new_card = game.cards.pop()
            # check card probability of acceptance
            print(f"\tdraws a {new_card.show()} card which costs {new_card.initial_carbon_cost} carbon credits to play")
            if new_card.acceptance_probability * 10 < dice.roll(10):
                print(f"\trefuses to play the {new_card.show()} card - returning it to the bottom of the deck")
                game.cards.insert(0, new_card)
            else:
                self.add_card(new_card)
                self.carbon_credits -= new_card.initial_carbon_cost

        # If no card is taken still do carbon calculations
        print(f"\tcurrent cards: {self.all_cards_str()}")
        carbon_lost = dice.roll(game.max_credits_lost_per_turn)
        print(f"\tLoses {carbon_lost} carbon credits this round")
        for card in self.cards:
            carbon_lost += card.carbon_per_turn()
        verb = "loses" if carbon_lost > 0 else "gains"
        print(f"{self.name} {verb} {carbon_lost} carbon credits")
        self.carbon_credits -= carbon_lost
        print("\n")

    def all_cards_str(self):
        """Prints the cards in the players hand"""
        s = ""
        for card in self.cards:
            s += f"{card.show()} "
        return s

    def possible_nuclear_meltdown(self):
        """There is a chance of a nuclear meltdown for each nuclear card in the players hand"""
        for card in self.cards:
            if card.show() == "[☢️]":
                if dice.roll(10) == 10 * card.disaster_probability:
                    print(f"\t{self.name} has a nuclear meltdown and loses all the carbon credits")
                    self.carbon_credits -= abs(self.carbon_credits)

    def final_score(self):
        """Returns the final score of the player is carbon credits plus the carbon value of each development card."""
        return self.carbon_credits + sum([card.final_credit for card in self.cards])
