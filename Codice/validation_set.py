from albero_di_decisione import *
import fpformat
from random import shuffle

def validation_set(dataset, attributi, target, percentuale, profondita,min_foglie_campione, num_test):
    # La funzione divide il dataset in trainset e validation set a seconda della percentuale
    # passata per parametro la profondita serve per il pruning


    #POTREI FARE UN INTERVALLO DI PERCENTUALI E MISURARE L'ACCURATEZZA CON L'ENTROPIA
    #QUEST OPERAZIONE FA FARE CON PRUNING E SENZA PRUNING E STAMPARE DUE GRAFICI
    #CON ASCISSA PERCENTUALE DI TRAIN RISPETTO AL TEST E ORDINATA ACCURATEZZA ENTROPIA
    numero_esempi = (int) (len(dataset)*percentuale)
    # Si inizializzano le variabili
    validation_set = []
    tmp = []
    accuratezza_train_tot = 0.0
    accuratezza_validation_tot = 0.0

    for test in range(num_test):
        shuffle(dataset)
        train_set = dataset[:]
        # I seguenti cicli permettono di dividere trainset e testset in base a una percentuale
        for i in range(0, numero_esempi):
            tmp.append(train_set.pop(0))
        for i in range(len(train_set)):
            validation_set.append(train_set.pop(0))
        train_set.extend(tmp)

        # Si crea l'albero di decisione usando il trainset
        albero = crea_albero_decisione(train_set, attributi, target, None, profondita, min_foglie_campione)

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
        accuratezza_train = 0.0
        accuratezza_validation = 0.0
        for i in train_set:
            #IMPORTANTISSIMO!!!!!!!!!!!
            #GUARDARE BENE QUESTO IF
            #if getValoreTarget(albero, i) is not None :
            if get_valore_target(albero, i) == i[target]:
                accuratezza_train = accuratezza_train + 1.0
        accuratezza_train_tot = accuratezza_train_tot + (accuratezza_train / len(train_set))
        # Si calcola lo score dell'albero in base ai dati del validation set
        for i in validation_set:
            #if getValoreTarget(albero, i) is not None :
            if get_valore_target(albero, i) == i[target]:
                accuratezza_validation = accuratezza_validation + 1.0
        accuratezza_validation_tot = accuratezza_validation_tot + (accuratezza_validation / len(validation_set))

    #ritorna l'accuratezza
    return [fpformat.fix(accuratezza_train_tot/num_test,4),fpformat.fix(accuratezza_validation_tot/num_test,4)]


def get_valore_target(albero, riga):
    # La funzione controlla se il tipo dell'albero e' una stringa. Se cosi' non e' vuol dire che non siamo arrivati
    # ad una foglia e che bisogna continuare la visita dell'albero.
    if type(albero) == type("string"):
        return albero
    else:
        attribute = albero.keys()[0]
        # Se il valore di attribute non viene trovato nel sotto albero la funzione ritorna None in modo da indicare
        # al livello superiore che l'albero non riesce a trovare una soluzione per line
        if riga[attribute] not in albero[attribute].keys():
            return None
        else:
            valore = albero[attribute][riga[attribute]]

        return get_valore_target(valore, riga)
