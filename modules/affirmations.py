import random

AFFIRMATIONS = [
    "You are building something meaningful.",
    "Your persistence is your superpower.",
    "Every line of code brings you closer to impact."
]

def get_affirmation():
    return random.choice(AFFIRMATIONS)
