"""
I encoded this program myself, did not copy or rewrite the code of others,
and did not give or send it to anyone else.
Do Chau Tuan
"""

# import numpy as np
import random
# import pandas as pd


def monte_carlo_simulation(n):
    attacker, draw, defender = 0, 0, 0
    for _ in range(n):
        score = 0
        player_1 = sorted([random.randint(1, 6) for _ in range(3)], reverse=True)[:2]
        player_2 = sorted([random.randint(1, 6) for _ in range(2)], reverse=True)
        for x, y in zip(player_1, player_2):
            if x > y:
                score += 1
            else:
                score -= 1
        if score > 0:
            attacker += 1
        elif score == 0:
            draw += 1
        else:
            defender += 1
    return [attacker / n, draw / n, defender / n]


def probability():
    attacker, draw, defender = 0, 0, 0
    sample_space_attacker = [sorted([x, y, z], reverse=True)[:2] for x in range(1, 7)
                             for y in range(1, 7) for z in range(1, 7)]
    sample_space_defender = [sorted([x, y], reverse=True) for x in range(1, 7)
                             for y in range(1, 7)]
    for x in range(len(sample_space_attacker)):
        for y in range(len(sample_space_defender)):
            score = 0
            for i, j in zip(sample_space_attacker[x], sample_space_defender[y]):
                if i > j:
                    score += 1
                else:
                    score -= 1
            if score > 0:
                attacker += 1
            elif score == 0:
                draw += 1
            else:
                defender += 1
    return [attacker / (6**5), draw / (6**5), defender / (6**5)]


def main():

    thousand_simulation = monte_carlo_simulation(1000)
    million_simulation = monte_carlo_simulation(1000000)
    prob = probability()
    print(f"{'Attacker': >30}{' ': <2}{'Draw': <10}{'Defender'}")
    print(f"{'1000 experiments': <22}{f'{thousand_simulation[0]:.5f}':<10}{f'{thousand_simulation[1]:.5f}':<10}"
          f"{f'{thousand_simulation[2]:.5f}'}")
    print(f"{'1000000 experiments': <22}{f'{million_simulation[0]:.5f}':<10}{f'{million_simulation[1]:.5f}':<10}"
          f"{f'{million_simulation[2]:.5f}'}")
    print(f"{'Probability': <22}{f'{prob[0]:.5f}': <10}{f'{prob[1]:.5f}': <10}{f'{prob[2]:.5f}'}")


if __name__ == "__main__":

    main()

