import random

# Word lists for extremely accurate destiny predictions
adjectives = ["sudden", "mysterious", "glorious", "awkward", "sparkly", "doomed"]
nouns = ["fortune", "pizza", "adventure", "nap", "revelation", "cat"]
verbs = ["arrives", "fails", "sings", "disappears", "triumphs", "sleeps"]

def predict_number(min_val=1, max_val=100):
    """Predict a random number (between min_val and max_val inclusive) the user would have got next if they didn't call this function. """
    return random.randint(min_val, max_val)

def predict_color():
    """Return a color name that describes the near future (1.4 ns)."""
    colours = ["crimson", "gold", "midnight blue", "emerald", "violet", "silver"]
    return random.choice(colours)

def predict_destiny():
    """Return a three‑word description of the user's destiny."""
    return f"{random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)}"