import csv
import numpy as np
from numpy import genfromtxt

a = np.genfromtxt('questao5.csv', delimiter=",")
mediaDeCadaColuna = []

def salvaCSV(a):
    write = csv.writer(open("salvandoCSVquestao5.csv", "w"))
    write.writerows(a)

def calculaMedia():
    global a
    global mediaDeCadaColuna 
    mediaDeCadaColuna = np.average(a, axis=0)
    #print(mediaDeCadaColuna)
    
def desvioMedioAbsoluto():
    global a
    global mediaDeCadaColuna
    coluna = 0
    listaAux = []
    listaAux2 = []
    somaDMA = 0

    while coluna < a.shape[1]:
        for linha in range(0, a.shape[0]):
            listaAux.append(abs(a[linha][coluna] - mediaDeCadaColuna[coluna])/a.shape[0])
        coluna = coluna + 1
    
    while(True):  

        if len(listaAux) == 0:
            break

        i = 0
        while i < a.shape[0] - 1:
            somaDMA = listaAux[i] + somaDMA
            i = i + 1
        
        del(listaAux[0:4])
        listaAux2.append(somaDMA)
        somaDMA = 0
     
    return listaAux2
     
def zScore():
    global a
    global mediaDeCadaColuna
    coluna = 0
    desvioMA = desvioMedioAbsoluto()
    #print(a)
    #print(mediaDeCadaColuna)
    #print(desvioMA)

    while True:
        for i in range(0, a.shape[0]):

            a[i][coluna] = (a[i][coluna] - mediaDeCadaColuna[coluna])/desvioMA[coluna]

        coluna = coluna + 1

        if coluna > 2:
            break
    
    print("zScore: \n", a)
    salvaCSV(a)


calculaMedia()
desvioMedioAbsoluto()
zScore()