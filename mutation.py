from numpy.random import normal as N
from math import exp, sqrt


def mutation_case1(chromosome):

    sigma = chromosome[-1]
    mutationed = []
    n = len(chromosome)

    epson_0 = 0.2
    learning_rate = 1 / sqrt(n)
    sigma_line = sigma * exp(learning_rate * N(0, 1))

    if sigma_line < epson_0:
        sigma_line = epson_0

    for xi in chromosome[0:-1]:
        mutationed.append(xi + sigma_line * N(0, 1))

    return mutationed

if __name__ == '__main__':

    print(mutation_case1(list(range(31))))