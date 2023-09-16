"""
I encoded this program myself, did not copy or rewrite the code of others,
and did not give or send it to anyone else.
Do Chau Tuan
"""
# In this example I will denote head by 0 and tail by 1
# import numpy as np
import random


def monte_carlo_simulation(n):

    total_payout = 0
    for _ in range(n):
        x = random.choice([0, 1])
        k = 1
        while x == 0:
            x = random.choice([0, 1])
            k += 1
        total_payout += 2 ** k

    return total_payout / n


def main():
    print(f'{monte_carlo_simulation(100):.3f}', f'{monte_carlo_simulation(10000):.3f}',
          f'{monte_carlo_simulation(1000000):.3f}')


if __name__ == "__main__":

    main()
