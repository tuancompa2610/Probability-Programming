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
def model1(n):
    # jn is a list of the x coordinates of the steps, rel is list of the values of the cdf
    return [jn, rel]


# Model 2
def model2(n):
    # jn is a list of the x coordinates of the steps, rel is list of the values of the cdf
    return [jn, rel]


# Model 3
def model3(n):
    # jn is a list of the x coordinates of the steps, rel is list of the values of the cdf
    return [jn, rel]


def main():
    n = int(sys.argv[1])
    plt.step(model1(n)[0], model1(n)[1])
    plt.step(model2(n)[0], model2(n)[1])
    plt.step(model3(n)[0], model3(n)[1])
    plt.show()


if __name__ == "__main__":
    main()