import sys

import math


def creaAlberoDecisione(dataset, attributi, target, parentDataset):
    valori = [i[target] for i in dataset]

    # EVENTUALMENTE TOGLIERE QUESTA PARTE DEL PLURALITY !!!!!!!!
    # Se il dataset e' vuoto o non ci sono attributi oltre a quello target si ritorna il valore di target
    # ripetuto piu' volte
    if not dataset:
        return pluralityValue(parentDataset, target)
    elif (len(attributi) - 1) <= 0:
        return pluralityValue(dataset, target)
    #EVENTUALMENTE TOGLIERE QUESTA PARTE DEL PLURALITY !!!!!!!!


    # Se il valore di target sono tutti uguali non ce' bisogno di continuare la produzione di sottoalberi
    # e si ritorna il primo valore della lista valori
    elif valori.count(valori[0]) == len(valori):
        return valori[0]

    # Se non siamo nei casi precedenti si effettua la ricerca del miglior attributo con importance
    # e si crea un sotto albero per ogni valore di bestAttributo
    else:
        bestAttributo = importanza(dataset, attributi, target)
        albero = {bestAttributo:{}} #creo dizionario

        tmp = []
        for i in dataset:
            if tmp.count(i[bestAttributo]) != 1:
                tmp.append(i[bestAttributo])

        for i in tmp:
            subAttributi = [attr for attr in attributi if attr != bestAttributo]
            exs = getSubDataset(dataset, bestAttributo, i)
            sotto_albero = creaAlberoDecisione(exs, subAttributi, target, dataset)
            albero[bestAttributo][i] = sotto_albero

    return albero


def pluralityValue(dataset, target):
    # La funzione ritorna il valore ripetuto piu' volte di target
    vals = [i[target] for i in dataset]
    maxFreq = 0
    valoreFrequente = None

    # Il seguente ciclo permette di avere una lista di valori non ripetuti
    tmp = []
    for i in dataset:
        if tmp.count(i[target]) != 1:
            tmp.append(i[target])

    for i in tmp:
        if vals.count(i) > maxFreq:
            maxFreq = vals.count(i)
            valoreFrequente = i

    return valoreFrequente

def importanza(dataset, attributi, target):
    # La funzione determina dato un attributo target, un insieme di attributi e un dataset
    # qual'e' l'attributo con information gain maggiore in base all'entropia

    # Il gain viene inizializzato a -1 perche' in alcuni casi di
    # classificazione tutti gli attributi hanno gain pari a 0
    bestGain = -1.0
    bestAttributo = None

    # Per ogni attributo chiamo il metodo di calcolo del gain in base all'impurita'
    for i in attributi:
        sys.stdout.write("\r{0}".format("Calcolo guadagno di:" + str(i)))
        sys.stdout.flush()

        tmpGain = gain(dataset, i, target)

        # Se il gain trovato e' maggiore del massimo precedente salvo il valore e il relativo attributo
        if tmpGain >= bestGain and i != target:
            bestGain = tmpGain
            bestAttributo = i
    return bestAttributo

def getSubDataset(data, attribute, value):
    # La funzione cerca tra i record di data quelli che hanno un certo valore per un certo attributo
    subDataset = []
    for i in data:
        if i[attribute] == value:
            subDataset.append(i)
    # Viene ritornao il subDataset usato per la creazione di un sotto albero
    return subDataset

def gain(dataset, attributi, target):
    # La funzione permette il calcolo dell'information gain di un attributo
    lista_frequenze = getFrequenzaValori(dataset, attributi)

    # Il seguente ciclo permette il calcolo del secondo termine della formula dell'information gain
    secondo_termine = 0.0
    for valori in lista_frequenze.keys():
        tmp = entropia([i for i in dataset if i[attributi] == valori], target)
        secondo_termine = secondo_termine + ((lista_frequenze[valori] / sum(lista_frequenze.values())) * tmp)

    # Viene ritornato il costo dell'intero dataSet rispetto al target - il termine calcolato precedentemente
    return entropia(dataset, target) - secondo_termine

#!!!! METTERE LA FUNZIONE ENTROPIA DENTRO IL GAIN!!!!!!!
def entropia(dataset, target):
    # La funzione calcola l' entropia di un attributo rispetto al dataSet

    lista_frequenze = getFrequenzaValori(dataset, target)
    entropia = 0.0
    for i in lista_frequenze.values():
        entropia = entropia + (-i / len(dataset)) * math.log(i / len(dataset), 2)

    return entropia
#!!!! METTERE LA FUNZIONE ENTROPIA DENTRO IL GAIN!!!!!!!

def getFrequenzaValori(data, attribute):
    # La funzione crea un dizionario dove ad ogni possibile valore di attributo viene associata la sua frequenza
    lista_frequenze = {}

    for i in data:
        if (lista_frequenze.has_key(i[attribute])):
            lista_frequenze[i[attribute]] += 1.0
        else:
            lista_frequenze[i[attribute]] = 1.0

    return lista_frequenze

def stampa_albero(albero, str):
    #LA FUNZIONE SCORRE L'ALBERO RICORSIVAMENTE E LO STAMPA
    if type(albero) == dict:
        print "%s%s" % (str, albero.keys()[0])
        for item in albero.values()[0].keys():
            print "%s\t%s" % (str, item)
            stampa_albero(albero.values()[0][item], str + "\t")
    else:
        print "%s\t->\t%s" % (str, albero)

def pruna_albero(albero):
    #IMPLEMENTARE UNA FUNZIONE CHE PRUNA UN ALBERO DI DECISIONE
    print "Applico pruning"