import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial

RANGE = 50


def plot(x, y, text):
    p = plt.plot(x, y)

    ar = sorted((i, j) for i, j in zip(x, y) if j <= RANGE)
    i, j = sorted(ar)[-1]

    min_y = RANGE if len(ar) != len(y) else 0
    j = max(j, min_y)

    plt.text(i, j, text, fontsize=12, color=p[0].get_color())


if __name__ == "__main__":
    x = np.arange(0, RANGE, 0.1)

    plot(x, np.ones(len(x)), "$1$")
    plot(x, np.log2(x), "$log(n)$")
    plot(x, np.sqrt(x), "$sqrt(n)$")
    plot(x, x, "$n$")
    plot(x, x * np.log2(x), "$n log(n)$")
    plot(x, x**2, "$n^{2}$")
    plot(x[:100], 2 ** x[:100], r"$2^{n}$")
    plot(x[:60], factorial(x[:60]), "$n!$")
    plot(x[:50], x[:50] ** x[:50], "$n^{n}$")

    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_xlim([0, RANGE])
    ax.set_ylim([0, RANGE])
    plt.gcf().set_size_inches(10, 10)
    plt.savefig("growth.png", dpi=100)
    plt.show()
