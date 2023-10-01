"""
I encoded this program myself, did not copy or rewrite the code of others,
and did not give or send it to anyone else.
Do Chau Tuan
"""
import random
import math
import matplotlib.pyplot as plt
import sys


# Model 1
# n is the number of experiments
def dis(x_1, y_1, x_2, y_2):
    return math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)


def model1(n):
    # jn is a list of the x coordinates of the steps, rel is list of the values of the cdf
    rel = [0] + [i / n for i in range(n+1)]
    jn = []
    for _ in range(n):
        r = random.uniform(-1, 1)
        jn.append(2 * math.sqrt(1 - r**2))
    jn.sort()
    jn = [0] + jn + [2]
    return [jn, rel]


# Model 2
def model2(n):
    # jn is a list of the x coordinates of the steps, rel is list of the values of the cdf
    rel = [0] + [i / n for i in range(n + 1)]
    jn = []
    x_1, y_1 = 1, 0
    for _ in range(n):
        alpha = random.uniform(0, math.pi)
        x_2, y_2 = math.cos(alpha), math.sin(alpha)
        jn.append(dis(x_1, y_1, x_2, y_2))
    jn.sort()
    jn = [0] + jn + [2]
    return [jn, rel]


# Model 3
def model3(n):
    # jn is a list of the x coordinates of the steps, rel is list of the values of the cdf
    rel = [0] + [i / n for i in range(n + 1)]
    jn = []
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        while dis(x, y, 0, 0) > 1:
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
        jn.append(2 * math.sqrt(1 - dis(x, y, 0, 0)**2))
    jn.sort()
    jn = [0] + jn + [2]
    return [jn, rel]


def main():
    n = int(sys.argv[1])
    plt.step(model1(n)[0], model1(n)[1])
    plt.step(model2(n)[0], model2(n)[1])
    plt.step(model3(n)[0], model3(n)[1])
    plt.show()


if __name__ == "__main__":
    main()