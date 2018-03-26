from albero_di_decisione import *
from decimal import *
from random import shuffle


def validation_set(dataset, attributi, target, percentuale, profondita):
    # La funzione divide il dataset in trainset e validation set a seconda della percentuale
    # passata per parametro la profondita serve per il pruning


    #POTREI FARE UN INTERVALLO DI PERCENTUALI E MISURARE L'ACCURATEZZA CON L'ENTROPIA
    #QUEST OPERAZIONE FA FARE CON PRUNING E SENZA PRUNING E STAMPARE DUE GRAFICI
    #CON ASCISSA PERCENTUALE DI TRAIN RISPETTO AL TEST E ORDINATA ACCURATEZZA ENTROPIA
    numeroEsempi = (int) (len(dataset)*percentuale)
    # Si inizializzano le variabili
    trainSet = dataset[:]
    validationSet = []
    tmp = []

    # I seguenti cicli permettono di dividere trainset e testset in base a una percentuale
    for i in range(0, numeroEsempi):
        tmp.append(trainSet.pop(0))
    for i in range(len(trainSet)):
        validationSet.append(trainSet.pop(0))
    trainSet.extend(tmp)
    # Si crea l'albero di decisione usando il trainset
    albero = creaAlberoDecisione(trainSet, attributi, target, None, profondita)

    ''' DEBUG DATI CORRETTI
    print "NUMERO DATI:"+str(len(dataset))
    print "NUMERO ESEMPI:"+str(numeroEsempi)
    sys.stdout.write("VALIDATION SET")
    sys.stdout.flush()
    print 'TRAIN SET'
    print "Lunghezza TRAIN:"+str(len(trainSet))
    print "##############    TRAIN"
    #print trainSet
    print "##############    FINE TRAIN"
    print "LUNGHEZZA VALIDATION SET:"+str(len(validationSet))
    print "##############    TEST"
    #print validationSet
    print "##############    FINE TEST"
    print "PERCENTUALE DI APPRENDIMENTO:"+str(percentuale*100)+"%"
    #HA SENSO RIMISCHIARE I DATI?!?!?!
    # shuffle(albero)
    # print albero
    #stampa_albero(albero,"")
    '''

    #FUNZIONE USATA PER VEDERE l'ALBERO SU ESEMPI SEMPLICI
    accuratezza_train = 0.0
    for i in trainSet:
        #IMPORTANTISSIMO!!!!!!!!!!!1
        #GUARDARE BENE QUESTO IF
        #if getValoreTarget(albero, i) is not None :
        if getValoreTarget(albero, i) == i[target]:
            accuratezza_train = accuratezza_train + 1.0
    accuratezza_train = accuratezza_train / len(trainSet)
    # Si calcola lo score dell'albero in base ai dati del validation set
    accuratezza_validation = 0.0
    for i in validationSet:
        #if getValoreTarget(albero, i) is not None :
        if getValoreTarget(albero, i) == i[target]:
            accuratezza_validation = accuratezza_validation + 1.0

    accuratezza_validation = accuratezza_validation / len(validationSet)

    print ""
    print "Percentuale training:"+str(percentuale*100)+"%"
    #ritorna l'accuratezza
    return [Decimal(accuratezza_train).quantize(Decimal('0.0001')),Decimal(accuratezza_validation).quantize(Decimal('0.0001'))]


def getValoreTarget(albero, riga):
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

        return getValoreTarget(valore, riga)
