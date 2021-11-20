from operator import itemgetter
import csv
import numpy as np
from numpy import genfromtxt

distanciaEuclidianaClasse = []


def baseDeDados():
    with open('questao8.csv', 'r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv, delimiter=',')
        data = list(leitor)  # Converte os dados lidos em csv para o tipo list

        #convertendo largura e altura para float
        for linha in range(0, len(data) - 1):
            data[linha][0] = float(data[linha][0])
            data[linha][1] = float(data[linha][1])

        return data


#Coordenadas é uma lista contendo a subtração das coordenadas, já para aplicar na distância Euclidiana
def calculaDistanciaEuclidiana(coordenadas):
    global distanciaEuclidianaClasse
    distanciaEuclidiana = 0

    #Calculo da distância Euclidiana para 2 dimenssões
    for i in range(0, len(coordenadas) - 1):
        for j in range(0, len(coordenadas[0]) - 2):
            distanciaEuclidiana = (coordenadas[i][j]**2 + coordenadas[i][j+1]**2)**(1/2)

        distanciaEuclidianaClasse.append([distanciaEuclidiana, coordenadas[i][2]])


def KNN(K, registroParaClassificar):
    classe = ""
    coordenadas = []
    dados = baseDeDados()
    listaAux = []
    x = 0

    #Cacula a distantica euclidiana para cada registro da base de dados
    while x < len(registroParaClassificar) - 1:
        for i in range(0, len(dados) - 1):
            #Já faço direto a subtração das coordenadas da distância euclidiana, no caso x2-x1,y2-y1
            listaAux.append([registroParaClassificar[x] - dados[i][0],registroParaClassificar[x+1] - dados[i][1], dados[i][2]])

        x = x + 2
        calculaDistanciaEuclidiana(listaAux)
        listaAux.clear()
        distanciaEuclidianaOrdenada = sorted(distanciaEuclidianaClasse, key=itemgetter(0))
        setosa = 0
        verticolor = 0

        #Conta a quantidade de ocorrencias para um K específico
        for i in range(0, K):
            if distanciaEuclidianaOrdenada[i][1] == 'Setosa':
                #contar a quantidade de setosa
                setosa = setosa + 1
            else:
                #contar a quantidade de Verticolor
                verticolor = verticolor + 1

        if setosa > verticolor:
            print("A classe é Setosa!")
        else:
            print("A classe é Verticolor! ")
        
        distanciaEuclidianaClasse.clear()
    
def registrosParaClassificar():
    registroParaClassificar = []

    registroParaClassificar.append(0.52) # Verticolor
    registroParaClassificar.append(0.80)

    registroParaClassificar.append(0.50)  # Setosa
    registroParaClassificar.append(0.56)

    registroParaClassificar.append(0.50) # Setosa
    registroParaClassificar.append(0.55)

    registroParaClassificar.append(0.52) # Verticolor
    registroParaClassificar.append(0.65)

    registroParaClassificar.append(0.54) # Verticolor
    registroParaClassificar.append(0.68)

    registroParaClassificar.append(0.51) # Verticolor
    registroParaClassificar.append(0.64)

    registroParaClassificar.append(0.54) # Verticolor
    registroParaClassificar.append(0.67)

    registroParaClassificar.append(0.55) # Verticolor
    registroParaClassificar.append(0.65)

    registroParaClassificar.append(0.56) # Verticolor
    registroParaClassificar.append(0.66)

    registroParaClassificar.append(0.51) # Verticolor
    registroParaClassificar.append(0.68)

    registroParaClassificar.append(0.53) # Verticolor
    registroParaClassificar.append(0.67)

    registroParaClassificar.append(0.46) # Setosa
    registroParaClassificar.append(0.57)

    registroParaClassificar.append(0.49) # Setosa
    registroParaClassificar.append(0.58)

    return registroParaClassificar

def main():
    KNN(3, registrosParaClassificar())

main()

