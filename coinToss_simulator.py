# Coin Toss Simulator
import random


def cointoss():
    rand_i = random.randint(0, 1)
    outcomes = ["Heads", "Tails"]
    return outcomes[rand_i]


# Toss a coin 3 times
t1 = cointoss()
t2 = cointoss()
t3 = cointoss()
print(t1, t2, t3)
