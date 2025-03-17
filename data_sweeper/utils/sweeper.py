import random
import json

def get_random_affirmation():
    with open("data/affirmations.json", "r") as file:
        affirmations = json.load(file)
    return random.choice(affirmations)
