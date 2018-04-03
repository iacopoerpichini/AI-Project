import math

def create_decision_tree(dataset, attributes, target, parent_dataset, depth):
    values = [i[target] for i in dataset]
    # Se il dataset e' vuoto o non ci sono attributi oltre a quello target si ritorna il valore di target
    # ripetuto piu' volte
    if not dataset:
        return plurality_value(parent_dataset, target)
    elif (len(attributes) - 1) <= 0:
        return plurality_value(dataset, target)
    #controllo profondita' pruning!!!!!!!!!
    if depth == 0 :
        return plurality_value(dataset, target)
    # Se il valore di target sono tutti uguali non ce' bisogno di continuare la produzione di sottoalberi
    # e si ritorna il primo valore della lista valori
    elif values.count(values[0]) == len(values):
        return values[0]
    # Se non siamo nei casi precedenti si effettua la ricerca del miglior attributo con importanza migliore
    # e si crea un sotto albero per ogni valore di miglior_attributo
    else:
        best_attribute = importance(dataset, attributes, target)
        tree = {best_attribute:{}} #creo dizionario
        tmp = []
        for i in dataset:
            if tmp.count(i[best_attribute]) != 1:
                tmp.append(i[best_attribute])
        for i in tmp:
            sub_attributes = [attr for attr in attributes if attr != best_attribute]
            exs = get_sub_dataset(dataset, best_attribute, i)
            sub_tree = create_decision_tree(exs, sub_attributes, target, dataset, depth - 1)
            tree[best_attribute][i] = sub_tree
    return tree



def plurality_value(dataset, target):
    # La funzione ritorna il valore ripetuto piu' volte di target
    values = [i[target] for i in dataset]
    max_freq = 0
    freq_value = None
    # Il seguente ciclo permette di avere una lista di valori non ripetuti
    tmp = []
    for i in dataset:
        if tmp.count(i[target]) != 1:
            tmp.append(i[target])
    for i in tmp:
        if values.count(i) > max_freq:
            max_freq = values.count(i)
            freq_value = i
    return freq_value

def importance(dataset, attributes, target):
    # La funzione determina dato un attributo target, un insieme di attributi e un dataset
    # qual'e' l'attributo con information gain maggiore in base all'entropia
    # Il gain viene inizializzato a -1 perche' in alcuni casi di
    # classificazione tutti gli attributi hanno gain pari a 0
    best_gain = -1.0
    best_attribute = None
    # Per ogni attributo chiamo il metodo di calcolo del gain in base all'impurita'
    for i in attributes:
        '''
        #DEBUG
        sys.stdout.write("\r{0}".format("Calcolo guadagno di:" + str(i)))
        sys.stdout.flush()
        '''
        tmp_gain = gain(dataset, i, target)
        # Se il gain trovato e' maggiore del massimo precedente salvo il valore e il relativo attributo
        if tmp_gain >= best_gain and i != target:
            best_gain = tmp_gain
            best_attribute = i
    return best_attribute

def get_sub_dataset(data, attribute, value):
    # La funzione cerca tra i record di data quelli che hanno un certo valore per un certo attributo
    sub_dataset = []
    for i in data:
        if i[attribute] == value:
            sub_dataset.append(i)
    # Viene ritornao il sub_dataset usato per la creazione di un sotto albero
    return sub_dataset

def gain(dataset, attributes, target):
    # La funzione permette il calcolo dell'information gain di un attributo
    frequency_list = get_frequency_list(dataset, attributes)
    # Il seguente ciclo permette il calcolo del secondo termine della formula dell'information gain
    second_term = 0.0
    for values in frequency_list.keys():
        tmp = entropy([i for i in dataset if i[attributes] == values], target)
        second_term = second_term + ((frequency_list[values] / sum(frequency_list.values())) * tmp)
    # Viene ritornato il costo dell'intero dataSet rispetto al target - il termine calcolato precedentemente
    return entropy(dataset, target) - second_term

def entropy(dataset, target):
    # La funzione calcola l' entropia di un attributo rispetto al dataSet
    frequency_list = get_frequency_list(dataset, target)
    entropy = 0.0
    for i in frequency_list.values():
        entropy = entropy + (-i / len(dataset)) * math.log(i / len(dataset), 2)
    return entropy

def get_frequency_list(data, attributes):
    # La funzione crea un dizionario dove ad ogni possibile valore di attributo viene associata la sua frequenza
    frequency_list = {}
    for i in data:
        if (frequency_list.has_key(i[attributes])):
            frequency_list[i[attributes]] += 1.0
        else:
            frequency_list[i[attributes]] = 1.0
    return frequency_list

def print_tree(tree, str):
    #LA FUNZIONE SCORRE L'ALBERO RICORSIVAMENTE E LO STAMPA
    if type(tree) == dict:
        print "%s%s" % (str, tree.keys()[0])
        for item in tree.values()[0].keys():
            print "%s\t%s" % (str, item)
            print_tree(tree.values()[0][item], str + "\t")
    else:
        print "%s\t->\t%s" % (str, tree)

