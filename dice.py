from random import random

def roll(n: int):
    """Returns a random integer from 1 to n"""
    return int(random() * n) + 1
