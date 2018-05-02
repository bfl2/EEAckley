from random import randint


def recombination_2fixed_parents(parent_1, parent_2):

    """Cada gene do filho eh a média de cada gene dos pais"""

    zip_parents = zip(parent_1, parent_2)

    return [(x[0] + x[1])/2 for x in zip_parents]


def recombination_2fixed_random(parent_1, parent_2):

    """Cada gene do filho eh a escolha aleatoria do gene do primeiro ou segundo pai"""

    zip_parents = zip(parent_1, parent_2)

    return [x[randint(0, 1)] for x in zip_parents]


def recombination_all_parents(all_parents):

    """Cada gene do filho eh a média de cada gene dos pais escolhidos randomicamente"""

    tuple_list = []
    size = len(all_parents)

    for i in range(30):
        p1 = all_parents[randint(0, size - 1)]
        p2 = all_parents[randint(0, size - 1)]

        tuple_list.append((p1[i], p2[i]))

    return [(x[0] + x[1])/2 for x in tuple_list]


def recombination_all_random(all_parents):

    """Cada gene do filho eh a escolha aleatoria do gene do primeiro ou segundo pai
        escolhidos randomicamente"""

    tuple_list = []
    size = len(all_parents)

    for i in range(30):
        p1 = all_parents[randint(0, size - 1)]
        p2 = all_parents[randint(0, size - 1)]

        tuple_list.append((p1[i], p2[i]))

    return [x[randint(0, 1)] for x in tuple_list]


if __name__ == '__main__':

    p1 = list(range(30))
    p2 = list(range(30))

    p2.reverse()

    print(recombination_2fixed_parents(p1, p2))
    print(recombination_2fixed_random(p1, p2))
    print(recombination_all_parents([p1, p2]))

    print(recombination_2fixed_parents.__doc__)