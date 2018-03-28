import math


def crea_albero_decisione(dataset, attributi, target, parentDataset, profondita, min_foglie_campione):
    valori = [i[target] for i in dataset]

    # Se il dataset e' vuoto o non ci sono attributi oltre a quello target si ritorna il valore di target
    # ripetuto piu' volte
    if not dataset:
        return plurality_value(parentDataset, target)
    elif (len(attributi) - 1) <= 0:
        return plurality_value(dataset, target)
    #controllo profondita' pruning!!!!!!!!!
    if profondita == 0 :
        return plurality_value(dataset, target)

    # Se il valore di target sono tutti uguali non ce' bisogno di continuare la produzione di sottoalberi
    # e si ritorna il primo valore della lista valori
    elif valori.count(valori[0]) == len(valori):
        return valori[0]

    # Se non siamo nei casi precedenti si effettua la ricerca del miglior attributo con importance
    # e si crea un sotto albero per ogni valore di miglior_attributo
    else:
        miglior_attributo = importanza(dataset, attributi, target)
        albero = {miglior_attributo:{}} #creo dizionario

        tmp = []
        for i in dataset:
            if tmp.count(i[miglior_attributo]) != 1:
                tmp.append(i[miglior_attributo])

        for i in tmp:
            sub_attributi = [attr for attr in attributi if attr != miglior_attributo]
            exs = get_sub_dataset(dataset, miglior_attributo, i)
            #controllo per vedere se siamo con troppi campioni mi serve per il pruning
            if len(exs) < min_foglie_campione :
                return plurality_value(dataset,target)
            sotto_albero = crea_albero_decisione(exs, sub_attributi, target, dataset, profondita - 1, min_foglie_campione)
            albero[miglior_attributo][i] = sotto_albero

    return albero


def plurality_value(dataset, target):
    # La funzione ritorna il valore ripetuto piu' volte di target
    valori = [i[target] for i in dataset]
    max_freq = 0
    valore_frequente = None

    # Il seguente ciclo permette di avere una lista di valori non ripetuti
    tmp = []
    for i in dataset:
        if tmp.count(i[target]) != 1:
            tmp.append(i[target])

    for i in tmp:
        if valori.count(i) > max_freq:
            max_freq = valori.count(i)
            valore_frequente = i

    return valore_frequente

def importanza(dataset, attributi, target):
    # La funzione determina dato un attributo target, un insieme di attributi e un dataset
    # qual'e' l'attributo con information gain maggiore in base all'entropia

    # Il gain viene inizializzato a -1 perche' in alcuni casi di
    # classificazione tutti gli attributi hanno gain pari a 0
    best_gain = -1.0
    best_attributo = None

    # Per ogni attributo chiamo il metodo di calcolo del gain in base all'impurita'
    for i in attributi:
        '''
        #DEBUG
        sys.stdout.write("\r{0}".format("Calcolo guadagno di:" + str(i)))
        sys.stdout.flush()
        '''
        tmp_gain = gain(dataset, i, target)

        # Se il gain trovato e' maggiore del massimo precedente salvo il valore e il relativo attributo
        if tmp_gain >= best_gain and i != target:
            best_gain = tmp_gain
            best_attributo = i
    return best_attributo

def get_sub_dataset(data, attribute, value):
    # La funzione cerca tra i record di data quelli che hanno un certo valore per un certo attributo
    sub_dataset = []
    for i in data:
        if i[attribute] == value:
            sub_dataset.append(i)
    # Viene ritornao il sub_dataset usato per la creazione di un sotto albero
    return sub_dataset

def gain(dataset, attributi, target):
    # La funzione permette il calcolo dell'information gain di un attributo
    lista_frequenze = get_frequenza_valori(dataset, attributi)

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
    lista_frequenze = get_frequenza_valori(dataset, target)
    entropia = 0.0
    for i in lista_frequenze.values():
        entropia = entropia + (-i / len(dataset)) * math.log(i / len(dataset), 2)

    return entropia
#!!!! METTERE LA FUNZIONE ENTROPIA DENTRO IL GAIN!!!!!!!

def get_frequenza_valori(data, attributi):
    # La funzione crea un dizionario dove ad ogni possibile valore di attributo viene associata la sua frequenza
    lista_frequenze = {}
    for i in data:
        if (lista_frequenze.has_key(i[attributi])):
            lista_frequenze[i[attributi]] += 1.0
        else:
            lista_frequenze[i[attributi]] = 1.0

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

