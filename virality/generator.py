from main import score
import matplotlib.pyplot as plt
import numpy as np
from random import randint, choice


def add_score(squeaks):
    for squeak in squeaks:
        squeak["score"] = score(squeak, squeak["blocks_elapsed"])
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
    return round(choice(list(np.random.pareto(0.1, 1)) + [0]))


def main():
    # title & labels
    plt.title("Virality")
    plt.xlabel("blocks elapsed since published")
    plt.ylabel("score")

    # blocks elapsed
    x = np.arange(1, 1000)

    # plot
    for squeak in add_score(random_squeaks(10000)):
        plt.plot(x, squeak["score"] / x)

    # render
    plt.show()


if __name__ == "__main__":
    main()
