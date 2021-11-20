import csv
import pandas as pd
import math


dataset = pd.read_csv('C:/Users/Railson Martins/Documents/9 Período/Mineração de Dados/Lista8_Respostas/inadimplencia.csv', sep=',')
naoInadimplentes = 0

def calculaMediaDeInadimplentes(dataset):
    dataset = dataset[(dataset['inadimplente'] == 'sim')]
    media = dataset['renda'].mean()
    return media

def calculaMediaDeNaoInadimplentes(dataset):
    dataset = dataset[(dataset['inadimplente'] == 'não')]
    media = dataset['renda'].mean()
    return media

def calculaDesvioPadraoDeInadimplentes(dataset):
    dataset = dataset[(dataset['inadimplente'] == 'sim')]
    std = dataset['renda'].std()
    return std

def calculaDesvioPadraoDeNaoInadimplentes(dataset):
    dataset = dataset[(dataset['inadimplente'] == 'não')]
    std = dataset['renda'].std()
    return std

#primeiro parâmetro é o atributo númerico, que se deseja fazer a probabilidade
#segundo parâmetro é se a pessoa é ou não inadimplente
def calculaDaProbabilidade(a, b, dataset):

    if b == 'não':
        expoente = 2.72**(-((pow(a-calculaMediaDeNaoInadimplentes(dataset),2)))/(2*pow(calculaDesvioPadraoDeNaoInadimplentes(dataset),2)))
        probabilidade = 1/((math.sqrt(2*3.14))*calculaDesvioPadraoDeNaoInadimplentes(dataset)) * expoente 
        return round(probabilidade, 4)   
    else:
        expoente = 2.72**(-((pow(a-calculaMediaDeInadimplentes(dataset),2)))/(2*pow(calculaDesvioPadraoDeInadimplentes(dataset),2)))
        probabilidade = 1/((math.sqrt(2*3.14))*calculaDesvioPadraoDeInadimplentes(dataset)) * expoente 
        return round(probabilidade, 4)


def classificaRegistro(casaPropria, estadoCivil, renda, dataset):
    global naoInadimplentes
    calculoProporcaoCasaPropriaNao = 0
    calculoProporcaoEstadoCivilNao = 0
    calculoProporcaoCasaPropriaSim = 0
    calculoProporcaoEstadoCivilSim = 0
    laplacde = 0
    probabilidadeParaNao = 0
    probabilidadeParaSim = 0
    print("=====================")
    print("Realizando classificação")

    #probabilidade para não
    calculoProporcaoCasaPropriaNao = (dataset.loc[(dataset['casa própria'] == casaPropria) & (dataset['inadimplente'] == 'não')].count()[0])/(dataset[dataset['inadimplente'] == 'não'].count()[0])
    calculoProporcaoEstadoCivilNao = (dataset.loc[(dataset['estado civil'] == estadoCivil) & (dataset['inadimplente'] == 'não')].count()[0])/(dataset[dataset['inadimplente'] == 'não'].count()[0])

    if calculoProporcaoCasaPropriaNao == 0 or calculoProporcaoEstadoCivilNao == 0:
        print("Calcula Laplace")
    else:
        probabilidadeParaNao = calculoProporcaoCasaPropriaNao * calculoProporcaoEstadoCivilNao * calculaDaProbabilidade(renda, 'não', dataset)


    #probabilidade para sim
    calculoProporcaoCasaPropriaSim = (dataset.loc[(dataset['casa própria'] == casaPropria) & (dataset['inadimplente'] == 'sim')].count()[0])/(dataset[dataset['inadimplente'] == 'sim'].count()[0])
    calculoProporcaoEstadoCivilSim = (dataset.loc[(dataset['estado civil'] == estadoCivil) & (dataset['inadimplente'] == 'sim')].count()[0])/(dataset[dataset['inadimplente'] == 'sim'].count()[0])

    if calculoProporcaoCasaPropriaSim == 0 or calculoProporcaoEstadoCivilSim == 0:
        print("Calcula Laplace")
    else:
        probabilidadeParaSim = calculoProporcaoCasaPropriaSim * calculoProporcaoEstadoCivilSim * calculaDaProbabilidade(renda, 'sim', dataset)
    
    #print("Probabilidade para sim: ", probabilidadeParaSim)

    if probabilidadeParaNao > probabilidadeParaSim:
        naoInadimplentes = naoInadimplentes + 1

def main():
    #parâmetros(casa própria, estado civil,renda, dados)
    classificaRegistro('não', 'casado', 120,dataset) #não
    classificaRegistro('não', 'solteiro', 70,dataset) #não
    classificaRegistro('sim', 'divorciado', 220,dataset) #não
    classificaRegistro('sim', 'solteiro', 125,dataset) #não
    classificaRegistro('não', 'solteiro', 85,dataset) #sim
    classificaRegistro('não', 'divorciado', 95,dataset) #sim

    print("Quantidade de registros classificados como não-inadimplentes: ", naoInadimplentes)


main()
