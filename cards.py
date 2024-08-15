import dice


class Card:

    def __init__(self, name, initial_carbon_cost, base_carbon_cost_per_round, carbon_cost_max_multiplier, acceptance_probability, disaster_probability, final_credit, symbol):
        self.name = name
        self.initial_carbon_cost = initial_carbon_cost
        self.base_carbon_cost_per_round = base_carbon_cost_per_round
        self.carbon_cost_max_multiplier = carbon_cost_max_multiplier
        self.acceptance_probability = acceptance_probability
        self.disaster_probability = disaster_probability
        self.final_credit = final_credit
        self.symbol = symbol

    def show(self):
        return f"[{self.symbol}]"

    def carbon_per_turn(self):
        if self.carbon_cost_max_multiplier == 0:
            return self.base_carbon_cost_per_round
        else:
            return self.base_carbon_cost_per_round + dice.roll(self.carbon_cost_max_multiplier)

