import EEAckley2 as ack2
import EEAckley as ack
import numpy as np
from matplotlib import pyplot as plt


def dummyDataset():

    avgFit = np.linspace(16,0,100)
    minFit = (16*np.exp(-avgFit))[::-1]
    indivFitness = [minFit,minFit,minFit]
    dataset = {"avgFit":avgFit,"minFit":minFit}

    return dataset


def plotGraf():

    dataset =  ack.EEAckley()

    print("AvgFit:{} | MinFit:{}".format(dataset["avgFitList"], dataset["minFit"]))
    #dataset = dummyDataset()
    fig, axes = plt.subplots(2, 2)
    x = np.linspace(0, dataset["generationCount"],dataset["generationCount"])
    y = dataset["avgFitList"]
    print(len(x),len(y))
    axes[0,0].plot(x,y)
    axes[0, 0].set_title("Media de fitness da versao 1")
    axes[0, 0].set_ylabel("Fitness Medio")
    axes[0, 0].set_xlabel("Geracao")

    dataset = ack2.EEAckley2()
    x = np.linspace(0, len(dataset["minFitList"]), len(dataset["minFitList"]))
    y = dataset["minFitList"]
    print(len(x), len(y))
    axes[0, 1].plot(x, y)
    axes[0, 1].set_title("Fitness Minimo da versao 1")
    axes[0, 1].set_ylabel("Fitness Minimo")
    axes[0, 1].set_xlabel("Geracao")


    print("AvgFit:{} | MinFit:{}".format(dataset["avgFitList"], dataset["minFit"]))
    #dataset = dummyDataset()
    x = np.linspace(0, dataset["generationCount"],dataset["generationCount"])
    y = dataset["avgFitList"]
    print(len(x),len(y))
    axes[1,0].plot(x,y)
    axes[1, 0].set_title("Media de fitness da versao 2")
    axes[1, 0].set_ylabel("Fitness Medio")
    axes[1, 0].set_xlabel("Geracao")

    #x = np.linspace(0, len(dataset["minFitList"]), len(dataset["minFitList"]))
    y = dataset["minFitList"]
    print(len(x), len(y))
    axes[1, 1].plot(x, y)
    axes[1, 1].set_title("Fitness Minimo da versao 2")
    axes[1, 1].set_ylabel("Fitness Minimo")
    axes[1, 1].set_xlabel("Geracao")





    plt.show()
    return


if __name__ == "__main__":
    plotGraf()