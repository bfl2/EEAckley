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

def get2RandomParents(allParents):
    indivSize = 30
    print("indivSize ", indivSize)
    i1 =0
    i2 =0
    while(i1==i2):
        i1 = random.randint(0,indivSize-1)
        i2 = random.randint(0,indivSize-1)
    parents = [allParents[i1],allParents[i2]]
    return parents


def generateChildren(allParents,childrenCount):
    sigma = 0.01
    children = []
    childrenList = []
    while (len(children)<childrenCount):
        parents = get2RandomParents(allParents)
        child = cross.recombination_all_parents(parents)
        ### A fazer, Analisar melhor como lidar com o formato [cromossomoL, fitness, sigma]
        if(len(child)<3):
            child = [child,sigma]
        child = mut.mutation_case1(child)
        children.append(child)

    ### Recalculando o fitness dos filhos, assumindo que os filhos estao no formato [cromossomo, fitness, sigma]
    for c in children:
        c[1] = fitness(c)
    childrenList = sorted(childrenList, key=itemgetter(1))
    print("children 1 len{}-{}".format(len(childrenList[0][0]),childrenList[0]))
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
    fit = -c1*np.exp(-c2*np.sqrt(sum1)) - np.exp(sum2) + c1 + np.e
    return round(fit,5)

def getAvgFit(pop):
    sum = 0
    for c in pop:
        sum+=c[1]
    return sum/len(pop)


def EEAckley():

    childrenCount = 700
    parentCount = 100
    generationCount = 0
    condSaida = False
    parents = generatePop(parentCount) # Populacao inicial
    minFit = parents[0][1]

    ##Listas de saida
    minFitList =[]
    avgFitList =[]


    while(condSaida == False):

        children = generateChildren(parents,childrenCount)
        parents = children[:parentCount]
        minFit = parents[0][1]
        avgFit = getAvgFit(parents)

        print("Geracao:{} Avg Fitness:{} / Max Fitness:{}".format(generationCount, avgFit,minFit))
        minFitList.append(minFit)
        avgFitList.append(avgFit)

        if(generationCount>40):
            condSaida=True
        generationCount += 1

    dataset = {"avgFitList":avgFitList, "minFitList":minFitList,"generation":generationCount,"minFit":minFit}
    print("Best solution{}-{}".format(len (parents[0][0]),parents[0][0]))
    return dataset


if __name__ == "__main__":
    EEAckley()
