import numpy as np
import matplotlib.pyplot as plt
import math


def fa(t):
    return (math.factorial(10) * t**7 * (1-t)**2) / (math.factorial(7) * math.factorial(2))


def fb(t):
    return (math.factorial(10) * t**6 * (1-t)**3) / (math.factorial(6) * math.factorial(3))


def main():

    X = []
    t = np.linspace(0, 1, 51)
    for _ in range(3000):
        arrival = []
        for _ in range(10):
            arrival.append(round(np.random.uniform(0, 1), 2))
        arrival.sort()
        X.append(arrival[7])

    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(3, 1, 1)
    ax1.hist(X, bins=50, density=1)

    ax2 = fig.add_subplot(3, 1, 2)
    ax2.plot(t, fa(t), color="r")

    ax3 = fig.add_subplot(3, 1, 3)
    ax3.plot(t, fb(t), color="g")

    fig.tight_layout()
    plt.show()
    print("a")


if __name__ == "__main__":
    main()