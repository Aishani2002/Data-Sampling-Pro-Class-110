import csv
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
import random
import pandas as pd

df= pd.read_csv("data.csv")
data= df["responses"].tolist()

mean= statistics.mean(data)
sd= statistics.stdev(data)

def randomSetOfMeans(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value= data[randomIndex]
        dataSet.append(value)
    mean= statistics.mean(dataSet)
    return mean

def showFig(meanList):
    df= meanList
    fig= ff.create_distplot([df],["Responses"],show_hist=False)
    fig.show()

def setup():
    meanList=[]
    for i in range(0,1000):
        setOfMeans= randomSetOfMeans(30)
        meanList.append(setOfMeans)
    mean= statistics.mean(meanList)
    mode= statistics.mode(meanList)
    median= statistics.median(meanList)
    stdev= statistics.stdev(meanList)
    showFig(meanList)
    print(mean)
    print(mode)
    print(median)
    print(stdev)

setup()