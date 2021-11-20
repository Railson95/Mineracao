from operator import itemgetter 


distanciaEuclidianaClasse = []

def baseDeDados():      
    iniciaBaseDados = [[0.47, 0.59, "Setosa"],
                       [0.52, 0.70, "Verticolor"],
                       [0.55, 0.72, "Verticolor"],
                       [0.45, 0.51, "Setosa"],
                       [0.46, 0.58, "Setosa"],
                       [0.52, 0.65, "Verticolor"],
                       [0.53, 0.64, "Verticolor"]]


    return iniciaBaseDados


#Coordenadas é uma lista contendo: x1,x2,y1,y2...xn-1,xn,yn-1,yn
#Que representa os valores dos atributos
def calculaDistanciaEuclidiana(coordenadas, classe):
    subtracaoDasCoordenadas = []
    global distanciaEuclidianaClasse
    distanciaEuclidiana = 0
    i = 0
    #Coloco em uma lista, a subtração dos atributos, para aplicar a distância euclidiana
    while(i < len(coordenadas)):
        subtracaoDasCoordenadas.append(coordenadas[i+1] - coordenadas[i])
        i = i + 2

    for i in range(0, len(subtracaoDasCoordenadas) - 1):
        distanciaEuclidiana = (subtracaoDasCoordenadas[i]**2 + subtracaoDasCoordenadas[i+1]**2)**(1/2)

    distanciaEuclidianaClasse.append([distanciaEuclidiana, classe])


def KNN(K):
    classe = ""
    coordenadas = []
    dados = baseDeDados()
    registroParaClassificar = []
    x = 0
    
    registroParaClassificar.append(0.50) # Setosa
    registroParaClassificar.append(0.56)

    registroParaClassificar.append(0.52) # Verticolor
    registroParaClassificar.append(0.80)
    
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

    #Cacula a distantica euclidiana para cada registro da base de dados
    while x <= len(registroParaClassificar) - 1:
        for i in range(0, len(dados)):
            coordenadas.append(dados[i][0])
            coordenadas.append(registroParaClassificar[x])
            coordenadas.append(dados[i][1])
            coordenadas.append(registroParaClassificar[x+1])
            
            classe = dados[i][2]

            calculaDistanciaEuclidiana(coordenadas, classe)

        x = x + 2
        #Ordena a distância euclidiana
        distanciaEuclidianaOrdenada = sorted(distanciaEuclidianaClasse, key=itemgetter(0))

        #Conta a quantidade de ocorrencias para um K específico
        for i in range(0, K):
            setosa = 0
            verticolor = 0
            if distanciaEuclidianaOrdenada[i][1] == "Setosa":
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


def main():
    KNN(3)
    
main()


