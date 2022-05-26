from math import log as ln, sqrt
import matplotlib.pyplot as plt
import numpy as np
from sample_data import squeaks


def score(x, squeak):
    if squeak["likes"] > 0 and squeak["resqueaks"] > 0:
        return 1000 / (x + virality(squeak) + 10)
    return 0 / x


def virality(squeak):
    ratio = sqrt(squeak["likes"] / max(squeak["dislikes"], 1))
    order = ln(squeak["likes"] + squeak["dislikes"]) * ratio
    amplifier = ln(squeak["resqueaks"]) / squeak["resqueaks"]
    virality = order * amplifier

    if virality == 0:
        return 0

    return 1 / virality


def main():
    # title & labels
    plt.title("Virality")
    plt.xlabel("blocks elapsed since published")
    plt.ylabel("score")

    # blocks elapsed
    x = np.arange(1, 1000)

    # plot
    for squeak in squeaks:
        plt.plot(x, score(squeak, x), label=squeak["label"])

    # render
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
