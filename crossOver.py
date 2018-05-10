from random import randint
from EEAckley import fitness

#   Input Format ([Chromosome, Fitness, sigma])
def recombination_2fixed_parents(parent1, parent2):

    """Cada gene do filho eh a média de cada gene dos pais"""

    parent_1 = parent1[0]
    parent_2 = parent2[0]

    sigma_1 = parent1[2]
    sigma_2 = parent2[2]

    zip_parents = zip(parent_1, parent_2)
    zip_sigmas = zip(sigma_1, sigma_2)

    child = [(x[0] + x[1])/2 for x in zip_parents]
    sigma_child = [(s[0] + s[1])/2 for s in zip_sigmas]

    fitness_child = fitness(child)

    return [child, fitness_child, sigma_child]


def recombination_2fixed_random(parent1, parent2):

    """Cada gene do filho eh a escolha aleatoria do gene do primeiro ou segundo pai"""
    parent_1 = parent1[0]
    parent_2 = parent2[0]

    sigma_1 = parent1[2]
    sigma_2 = parent2[2]

    zip_parents = zip(parent_1, parent_2)
    zip_sigmas = zip(sigma_1, sigma_2)

    child = [x[randint(0, 1)] for x in zip_parents]
    sigma_child = [(s[0] + s[1]) / 2 for s in zip_sigmas]

    fitness_child = fitness(child)

    return [child, fitness_child, sigma_child]


#   Receive a population of individuals
def recombination_all_parents(all_parents):

    """Cada gene do filho eh a média de cada gene dos pais escolhidos randomicamente"""

    tuple_parents = []
    tuple_sigmas = []
    size = len(all_parents)
    num_gene = len(all_parents[0][0])

    for i in range(num_gene):
        p1 = all_parents[randint(0, size - 1)]
        p2 = all_parents[randint(0, size - 1)]

        tuple_parents.append((p1[0][i], p2[0][i]))
        tuple_sigmas.append((p1[2][i], p2[2][i]))

    child = [(x[0] + x[1])/2 for x in tuple_parents]
    sigma_child = [(s[0] + s[1])/2 for s in tuple_sigmas]

    fitness_child = fitness(child)

    return [child, fitness_child, sigma_child]


def recombination_all_random(all_parents):

    """Cada gene do filho eh a escolha aleatoria do gene do primeiro ou segundo pai
        escolhidos randomicamente"""

    tuple_parents = []
    tuple_sigmas = []
    size = len(all_parents)
    num_gene = len(all_parents[0][0])

    for i in range(num_gene):
        p1 = all_parents[randint(0, size - 1)]
        p2 = all_parents[randint(0, size - 1)]

        tuple_parents.append((p1[0][i], p2[0][i]))
        tuple_sigmas.append((p1[2][i], p2[2][i]))

    child = [x[randint(0, 1)] for x in tuple_parents]
    sigma_child = [s[randint(0, 1)] for s in tuple_sigmas]

    fitness_child = fitness(child)

    return [child, fitness_child, sigma_child]


#   Basic Test
if __name__ == '__main__':

    p1 = [list(range(30)), 12.3, list(range(30))]
    p2 = [list(range(30)), 52.3, list(range(30))]

    pop = [p1, p2]
    print(recombination_2fixed_parents(p1, p2))
    print(recombination_all_parents(pop))

    print(recombination_2fixed_parents.__doc__)