"""
I encoded this program myself, did not copy or rewrite the code of others,
and did not give or send it to anyone else.
Do Chau Tuan
"""
# import numpy as np
import random
# In this example I will denote 3 distinct rooms by number 1, 2, 3


def keep():
    car = random.randint(1, 3)
    player = random.randint(1, 3)
    goat = random.randint(1, 3)
    while goat in {car, player}:
        goat = random.randint(1, 3)
    return player == car


def change():
    car = random.randint(1, 3)
    player = random.randint(1, 3)
    goat = random.randint(1,3)
    while goat in {car, player}:
        goat = random.randint(1, 3)
    new_choice = random.randint(1, 3)
    while new_choice in {goat, player}:
        new_choice = random.randint(1, 3)
    return new_choice == car


def prob():
    car = random.randint(1, 3)
    player = random.randint(1, 3)
    goat = random.randint(1, 3)
    while goat in {car, player}:
        goat = random.randint(1, 3)
    other_option = random.randint(1, 3)
    while other_option in [player, goat]:
        other_option = random.randint(1, 3)
    final_choice = random.choice([player, other_option])
    return final_choice == car


def main():

    keep_res, change_res, prob_res = 0, 0, 0
    n = 1000
    for _ in range(n):
        keep_res += keep()
        change_res += change()
        prob_res += prob()
    print(f"Keep the decision     {keep_res / n:.3f}")
    print(f"Change the decision   {change_res / n:.3f}")
    print(f"All the same          {prob_res / n:.3f}")


if __name__ == "__main__":

    main()
