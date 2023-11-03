import matplotlib.pyplot as plt
import numpy as np


def distribution_2(prob):
    dist = [0] * 13
    for x in range(1, 7):
        for y in range(1, 7):
            dist[x+y] += (prob[x-1] * prob[y-1])
    return dist


def distribution(prob, k):
    dist = [0] * (6*k + 1)
    dist[:13] = distribution_2(prob)
    for i in range(3, k+1):
        res = [0] * (6 * k + 1)
        for x in range(1, 7):
            for y in range(i-1, (i-1)*6+1):
                res[x+y] += (prob[x-1] * dist[y])
        dist = res
    return res[k:]


def main():

    prob = [0.3, 0.1, 0.05, 0.05, 0.15, 0.35]
    dist_2 = distribution_2(prob)
    dist_3 = distribution(prob, 3)
    dist_4 = distribution(prob, 4)
    dist_10 = distribution(prob, 10)
    dist_20 = distribution(prob, 20)
    fig, ax = plt.subplots(2, 3, figsize=(18, 9))
    ax[0, 0].bar(list(range(1, 7)), prob, color="r")
    ax[0, 1].bar(list(range(2, 6*2+1)), dist_2[2:], color="g")
    ax[0, 2].bar(list(range(3, 6*3+1)), dist_3, color="b")
    ax[1, 0].bar(list(range(4, 6*4+1)), dist_4, color="m")
    ax[1, 1].bar(list(range(10, 6*10+1)), dist_10, color="y")
    ax[1, 2].bar(list(range(20, 6*20+1)), dist_20, color="c")
    plt.show()

    return fig


if __name__ == "__main__":
    main()