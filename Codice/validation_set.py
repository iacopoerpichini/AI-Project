from albero_di_decisione import *
import fpformat
from random import shuffle

def validation_set(dataset, attributes, target, percentage, depth, min_sample_leaf, num_test):
    # La funzione divide il dataset in trainset e validation set a seconda della percentuale
    # passata per parametro la profondita e il minimo numero di foglie campione servono per il pruning
    # mentre il numero di test serve per fare test multipli e calcolare una media di valori
    num_examples = (int) (len(dataset) * percentage)
    # Si inizializzano le variabili
    validation_set = []
    tmp = []
    accuracy_train_tot = 0.0
    accuracy_validation_tot = 0.0

    for test in range(num_test):
        shuffle(dataset) # a ogni test si mischia il dataset
        train_set = dataset[:]
        # I seguenti cicli permettono di dividere trainset e testset in base a una percentuale
        for i in range(0, num_examples):
            tmp.append(train_set.pop(0))
        for i in range(len(train_set)):
            validation_set.append(train_set.pop(0))
        train_set.extend(tmp)
        # Si crea l'albero di decisione usando il trainset
        tree = create_decision_tree(train_set, attributes, target, None, depth, min_sample_leaf)
        ''' DEBUG DATI CORRETTI
        print "NUMERO DATI:"+str(len(dataset))
        print "NUMERO ESEMPI:"+str(numero_esempi)
        sys.stdout.write("VALIDATION SET")
        sys.stdout.flush()
        print 'TRAIN SET'
        print "Lunghezza TRAIN:"+str(len(train_set))
        print "##############    TRAIN"
        #print train_set
        print "##############    FINE TRAIN"
        print "LUNGHEZZA VALIDATION SET:"+str(len(validation_set))
        print "##############    TEST"
        #print validation_set
        print "##############    FINE TEST"
        print "PERCENTUALE DI APPRENDIMENTO:"+str(percentuale*100)+"%"
        #HA SENSO RIMISCHIARE I DATI?!?!?!
        # shuffle(albero)
        # print albero
        #stampa_albero(albero,"") #FUNZIONE USATA PER VEDERE l'ALBERO SU ESEMPI SEMPLICI
        '''
        accuracy_train = 0.0
        accuracy_validation = 0.0
        for i in train_set:
            #IMPORTANTISSIMO!!!!          GUARDARE BENE QUESTO IF
            #if get_target_value(tree, i) is not None : # vecchia versione
            if get_target_value(tree, i) == i[target]:
                accuracy_train = accuracy_train + 1.0
        accuracy_train_tot = accuracy_train_tot + (accuracy_train / len(train_set))
        # Si calcola lo score dell'albero in base ai dati presenti nel validation set
        for i in validation_set:
            #if get_target_value(tree, i) is not None :
            if get_target_value(tree, i) == i[target]:
                accuracy_validation = accuracy_validation + 1.0
        accuracy_validation_tot = accuracy_validation_tot + (accuracy_validation / len(validation_set))

    #ritorna l'accuratezza
    return [fpformat.fix(accuracy_train_tot/num_test,8),fpformat.fix(accuracy_validation_tot/num_test,8)]


def get_target_value(tree, row):
    # La funzione controlla se il tipo dell'albero e' una stringa. Se cosi' non e' vuol dire che non siamo arrivati
    # ad una foglia e che bisogna continuare la visita dell'albero.
    if type(tree) == type("string"):
        return tree
    else:
        attribute = tree.keys()[0]
        # Se il valore di attributo non viene trovato nel sotto albero la funzione ritorna None in modo da indicare
        # al livello superiore che l'albero non riesce a trovare una soluzione per line
        if row[attribute] not in tree[attribute].keys():
            values = []
            for key in tree[attribute].keys():
                values.append(get_target_value(tree[attribute][key], row))
            return max(values, key=values.count)
        else:
            value = tree[attribute][row[attribute]]

        return get_target_value(value, row)
