import crossOver
import mutation
import random
import numpy as np


def generateIndivI():
    n = 30
    indiv = []
    while (len(indiv) < n):
        indiv.append(round(random.randint(-15, 15), 5))

    return indiv
def generateIndiv():
    n = 30
    indiv = []
    while (len(indiv) < n):
        indiv.append(round(random.uniform(-15, 15), 5))

    return indiv

def fitness(chromossome):
    c1=20
    c2=0.2
    c3=2*np.pi
    sum1 = 0
    sum2 = 0
    for xi in chromossome:
        sum1+= xi**2
        sum2+= np.cos(c3*xi)
    sum1 = sum1/len(chromossome)
    sum2 = sum2/len(chromossome)
    fit = -c1*np.exp(-c2*np.sqrt(sum1)) - np.exp(sum2) + c1 + 1
    return round(fit,5)

def EEAckley():


    return


if __name__ == "__main__":
    EEAckley()