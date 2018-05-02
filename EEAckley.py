import crossOver as cross
import mutation as mut
import random
import numpy as np
from operator import itemgetter

def removeFit(pop):
    res =[]
    for e in pop:
        res.append(e[0])
    return res

def generateIndivI():
    n = 30
    indiv = []
    while (len(indiv) < n):
        indiv.append(round(random.randint(-15, 15), 5))

    return indiv


def generateIndiv():
    n = 30
    chromossome= []
    while (len( chromossome) < n):
        chromossome.append(round(random.uniform(-15, 15), 5))
    fit = fitness(chromossome)
    indiv = [chromossome,fit]
    return indiv

def generatePop(size):
    pop = []
    while (len(pop)< size):
        pop.append(generateIndiv())
    pop = sorted(pop, key=itemgetter(1))
    return pop

def generateChildren(parents,childrenCount):
    bareParents = removeFit(parents)
    children = []
    childrenList = []
    while (len(children)<childrenCount):
        child = cross.recombination_all_parents(bareParents)
        #child = mutation()
        children.append(child)

    for c in children:
        childrenList.append([c,fitness(c)])

    childrenList = sorted(childrenList, key=itemgetter(1))
    return childrenList

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

def getAvgFit(pop):
    sum = 0
    for c in pop:
        sum+=c[1]
    return sum/len(pop)


def EEAckley():

    childrenCount = 70
    parentCount = 10
    generationCount = 0
    condSaida = False
    parents = generatePop(parentCount) # Populacao inicial
    minFit = parents[0][1]

    while(condSaida == False):
        generationCount+=1
        children = generateChildren(parents,childrenCount)
        parents = children[:parentCount]
        minFit = parents[0][1]
        avgFit = getAvgFit(parents)

        print("Avg Fitness:{} / Max Fitness:{}".format( avgFit,minFit))

        if(generationCount>10):
            condSaida=True


    return


if __name__ == "__main__":
    EEAckley()