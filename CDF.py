"""
I encoded this program myself, did not copy or rewrite the code of others,
and did not give or send it to anyone else.
Do Chau Tuan
"""
import math
import random
import scipy.integrate as integrate
from fractions import Fraction

def F(x):

    if 0 <= x <= 1.5:
        return 2 * x**2 / 9
    else:
        return -x**2 + 4*x - 3


def G(x):
    # G = 1 - F for calculating the expected value
    if 0 <= x <= 1.5:
        return 1 - 2 * x**2 / 9
    else:
        return 1 - (-x**2 + 4*x - 3)






def monte_carlo_simulation():
    sample = []
    for _ in range(1000):
        u = random.uniform(0, 1)
        while 0.5 < u <= 0.75:
            u = random.uniform(0, 1)
        if u <= 0.5:
            x = math.sqrt(4.5 * u)
        else:
            x = -math.sqrt(1 - u) + 2
        sample.append(round(x, 3))
    return sample



def expect_value():
    return integrate.quad(G, 0, 2, )[0]


def main():
    X = monte_carlo_simulation()
    freq = 0
    for i in range(len(X)):
        if X[i] == 1.500:
            freq += 1
    print(f"{sum(X) / len(X):.5f}")
    print(f"{freq / len(X):.3f}")
    print(f"{expect_value():.5f}")
    print(Fraction(integrate.quad(F, 0, 1.5)[0]))


if __name__ == "__main__":
    main()