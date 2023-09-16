"""
I encoded this program myself, did not copy or rewrite the code of others,
and did not give or send it to anyone else.
Do Chau Tuan
"""
import matplotlib.pyplot as plt
import random as rd
import sys
import math


def comb(i, n):
    return math.factorial(n) // math.factorial(n - i) // math.factorial(i)


def binom_pmf(i, n, p):
    return comb(i, n) * p ** i * (1 - p) ** (n - i)


def poison_dist(i, n, p):
    l = n * p
    return l ** i * math.exp(-l) / math.factorial(i)


def monte_carlo_simulation(n, p, k):

    simulated = [0] * (n + 1)
    for _ in range(k):
        trial = [rd.randint(1, int(1 / p)) for i in range(n)]
        x = trial.count(1)
        for i in range(n + 1):
            if x == i:
                simulated[i] += 1

    return [i / k for i in simulated]


def main():

    n = int(sys.argv[1])
    p = float(sys.argv[2])
    k = int(sys.argv[3])
    interval = list(range(n + 1))
    binom = [binom_pmf(i, n, p) for i in interval]
    simulation = monte_carlo_simulation(n, p, k)
    poison = [poison_dist(i, n, p) for i in interval]

    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(3, 1, 1)
    ax1.bar(interval, binom)
    ax1.set_title("Binomial distribution")

    ax2 = fig.add_subplot(3, 1, 2)
    ax2.bar(interval, simulation)
    ax2.set_title("Binomial distribution simulated with 1000 experiments")

    ax3 = fig.add_subplot(3, 1, 3)
    ax3.bar(interval, poison)
    ax3.set_title("Binomial distribution approximated with Poisson-distribution")

    fig.tight_layout()
    plt.show()
    return fig


if __name__ == "__main__":
    main()
