from math import log, sqrt
import matplotlib.pyplot as plt
import numpy as np
from sample_data import squeaks


def limit(x, squeak):
    if squeak["likes"] > 0 and squeak["resqueaks"] > 0:
        return 1 / ((x) + virality(squeak))
    return 0 / x


def virality(squeak):
    ratio = squeak["likes"] / max(squeak["dislikes"], 1)
    total = log(squeak["likes"] + squeak["dislikes"], 10)
    amplifier = log(squeak["resqueaks"], 10)
    order = sqrt(ratio) * total * amplifier
    if order == 0:
        return 0
    return 1 / order


def main():
    # title & labels
    plt.title("Virality")
    plt.xlabel("blocks elapsed since authored")
    plt.ylabel("coefficient")

    # blocks elapsed
    x = np.arange(1, 50)

    # plot
    for squeak in squeaks:
        plt.plot(x, limit(x, squeak), label=squeak["label"])

    # render
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
