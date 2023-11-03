import sys

from matplotlib.patches import Ellipse    # modul for drawing
import matplotlib.pyplot as plt
import numpy as np


def main():
    matrix = np.array([int(sys.argv[i]) for i in range(1, 5)]).reshape(2, 2)
    covariance = np.dot(matrix, matrix.T)
    eig_vals, eig_vecs = np.linalg.eig(covariance)
    axis = 6 * np.sqrt(eig_vals)
    slope = eig_vecs[1][0] / eig_vecs[1][1]
    angle = 180 * np.arctan(slope) / np.pi
    sample = np.random.multivariate_normal((0, 0), covariance, 1000)
    x = sample[:, 0]
    y = sample[:, 1]
    ax = plt.subplot(aspect='equal')          # subfigure
    ell = Ellipse(xy=(0,0),                   # fill in!
                  width=axis[0],
                  height=axis[1],
                  edgecolor='r',
                  angle=angle)
    ell.set_facecolor('none')                 # be empty
    ax.add_artist(ell)
    plt.plot(x, y, 'x')                       # these are the dots
    plt.axis('equal')
    plt.show()


if __name__ == "__main__":
    main()