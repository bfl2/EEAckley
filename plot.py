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

def absAvg(list):
    sum=0
    for e in list:
        sum+=abs(e)
    res = sum/len(list)
    return res


def plotGraf():#plota o grafico rodando somente 1 vez o algoritmo

    dataset =  ack.EEAckley()

    print("AvgFit:{} | MinFit:{}".format(dataset["avgFitList"], dataset["minFit"]))
    #dataset = dummyDataset()
    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    stringData1 = "Fitness Medio: " + str(round(dataset["avgFit"], 5))
    stringData2 = "Fitness Minimo: " + str(round(dataset["minFit"], 5))
    stringData = stringData1+"\n"+stringData2

    x = np.linspace(0, dataset["generationCount"],dataset["generationCount"])
    #fitness medio
    y = dataset["avgFitList"]
    axes.plot(x,y,label="fitness medio")
    axes.set_title("Media e minimo de fitness da versao 1")
    axes.set_ylabel("Fitness")
    axes.set_xlabel("Geracao")
    axes.legend(loc=0)
    axes.text(0.9,0.8,stringData, horizontalalignment='center',verticalalignment='center',transform=axes.transAxes,bbox=dict(facecolor='blue', alpha=0.2))

    ##Fitness minimo
    x = np.linspace(0, len(dataset["minFitList"]), len(dataset["minFitList"]))
    y = dataset["minFitList"]
    axes.plot(x, y, label="fitness minimo")
    axes.legend(loc=0)
    axes.annotate(stringData2, (0, 0))


    plt.show()
    ###Versao 2###
    dataset = ack2.EEAckley2()

    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    print("AvgFit:{} | MinFit:{}".format(dataset["avgFitList"], dataset["minFit"]))
    stringData1 = "Fitness Medio: " + str(round(dataset["avgFit"], 5))
    stringData2 = "Fitness Minimo: " + str(round(dataset["minFit"], 5))
    stringData = stringData1 + "\n" + stringData2
    x = np.linspace(0, dataset["generationCount"],dataset["generationCount"])
    y = dataset["avgFitList"]
    axes.plot(x,y, label="fitness medio")
    axes.set_title("Media e minimo de fitness da versao 2")
    axes.set_ylabel("Fitness")
    axes.set_xlabel("Geracao")
    axes.legend(loc=0)
    axes.text(0.9, 0.8, stringData, horizontalalignment='center', verticalalignment='center', transform=axes.transAxes,
              bbox=dict(facecolor='blue', alpha=0.2))


    x = np.linspace(0, len(dataset["minFitList"]), len(dataset["minFitList"]))
    y = dataset["minFitList"]

    axes.plot(x, y,label="fitness minimo")
    axes.legend(loc=0)



    plt.show()
    return

def plotGrafRep(reps):
    minFitList = []
    avgFitList = []
    xiAbsAvgList = []

    for e in range(0,reps): ## calculando as medias dos fitness minimo e medio finais do algoritmo
        dataset =  ack.EEAckley()
        minFitList.append(dataset["minFit"])
        avgFitList.append(dataset["avgFit"])
        xiAbsAvgList.append(absAvg(dataset["bestIndiv"]))

    avgFitListMean = sum(avgFitList)/len(avgFitList)
    avgFitListStd = np.std(avgFitList)
    minFitListMean = sum(minFitList)/len(minFitList)
    minFitListStd = np.std(minFitList)


    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    stringData1 = "Resultados de {} repetiçoes".format(reps)
    stringData2 = "Fitness Medio:{} || Desvio padrao:{}".format(round(avgFitListMean, 5),round(avgFitListStd, 5))
    stringData3 = "Fitness Minimo:{} || Desvio padrao:{}".format(round(minFitListMean, 5),round(minFitListStd, 5))
    stringData4 = "Media dos elementos do cromossomo:{}".format(round(absAvg(dataset["bestIndiv"]), 5))
    stringData = stringData1 + "\n" + stringData2 + "\n" + stringData3+"\n" + stringData4

    x = np.linspace(0, dataset["generationCount"],dataset["generationCount"])
    #fitness medio
    y = dataset["avgFitList"]
    axes.plot(x,y,label="fitness medio")
    axes.set_title("Media e minimo de fitness da versao 1")
    axes.set_ylabel("Fitness")
    axes.set_xlabel("Geracao")
    axes.legend(loc=0)
    axes.text(0.8,0.8,stringData, horizontalalignment='center',verticalalignment='center',transform=axes.transAxes,bbox=dict(facecolor='blue', alpha=0.2))

    ##Fitness minimo
    x = np.linspace(0, len(dataset["minFitList"]), len(dataset["minFitList"]))
    y = dataset["minFitList"]
    axes.plot(x, y, label="fitness minimo")
    axes.legend(loc=0)
    axes.annotate(stringData2, (0, 0))


    plt.show()
    ###Versao 2###
    minFitList = []
    avgFitList = []
    xiAbsAvgList = []
    for e in range(0, reps):  ## calculando as medias dos fitness minimo e medio finais do algoritmo
        dataset = ack2.EEAckley2()
        minFitList.append(dataset["minFit"])
        avgFitList.append(dataset["avgFit"])
    avgFitListMean = sum(avgFitList) / len(avgFitList)
    avgFitListStd = np.std(avgFitList)
    minFitListMean = sum(minFitList) / len(minFitList)
    minFitListStd = np.std(minFitList)

    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    stringData1 = "Resultados de {} repetiçoes".format(reps)
    stringData2 = "Fitness Medio:{} || Desvio padrao:{}".format(round(avgFitListMean, 5), round(avgFitListStd, 5))
    stringData3 = "Fitness Minimo:{} || Desvio padrao:{}".format(round(minFitListMean, 5), round(minFitListStd, 5))
    stringData4 = "Media dos elementos do cromossomo:{}".format(round(absAvg(dataset["bestIndiv"]), 5))
    stringData = stringData1 + "\n" + stringData2 + "\n" + stringData3 + "\n" + stringData4
    x = np.linspace(0, dataset["generationCount"],dataset["generationCount"])
    y = dataset["avgFitList"]
    axes.plot(x,y, label="fitness medio")
    axes.set_title("Media e minimo de fitness da versao 2")
    axes.set_ylabel("Fitness")
    axes.set_xlabel("Geracao")
    axes.legend(loc=0)
    axes.text(0.9, 0.8, stringData, horizontalalignment='center', verticalalignment='center', transform=axes.transAxes,
              bbox=dict(facecolor='blue', alpha=0.2))


    x = np.linspace(0, len(dataset["minFitList"]), len(dataset["minFitList"]))
    y = dataset["minFitList"]

    axes.plot(x, y,label="fitness minimo")
    axes.legend(loc=0)



    plt.show()
    return


if __name__ == "__main__":
    #plotGraf()
    plotGrafRep(5)