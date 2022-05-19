import matplotlib.pyplot as plt
import numpy as np
from random import randint, choice
from main import limit


def add_limit(squeaks):
    for squeak in squeaks:
        squeak["limit"] = limit(squeak["blocks_elapsed"], squeak)
    return squeaks


def random_squeak():
    return {
        "likes": weighted_random(),
        "dislikes": weighted_random(),
        "resqueaks": weighted_random(),
        "blocks_elapsed": randint(1, 50),
    }


def random_squeaks(count):
    return [random_squeak() for _ in range(count)]


def weighted_random():
    return round(choice(list(np.random.pareto(0.1, 5)) + [0]))


def main():
    # title & labels
    plt.title("Virality")
    plt.xlabel("blocks elapsed since authored")
    plt.ylabel("coefficient")

    # blocks elapsed
    x = np.arange(1, 50)

    # plot
    for squeak in add_limit(random_squeaks(10000)):
        plt.plot(x, squeak["limit"] / x)

    # render
    plt.show()


if __name__ == "__main__":
    main()
