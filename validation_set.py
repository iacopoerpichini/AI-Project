from albero_di_decisione import *
from decimal import *


def validation_set(dataset, attributi, target, percentuale,pruning):
    #SCRIVERE L'ALG DI APPRENDIMENTO ALBERI CON E SENZA PRUNING
    #A SECONDA DEL VALORE CHE PASSERO' PER PARAMETRO
    if pruning == 0 :
        print "SENZA PRUNING"
    else:
        print "CON PRUNING"
    # La funzione divide il dataset in trainset e validation set a seconda della percentuale
    # passata per parametro


    #POTREI FARE UN INTERVALLO DI PERCENTUALI E MISURARE L'ACCURATEZZA CON L'ENTROPIA
    #QUEST OPERAZIONE FA FARE CON PRUNING E SENZA PRUNING E STAMPARE DUE GRAFICI
    #CON ASCISSA PERCENTUALE DI TRAIN RISPETTO AL TEST E ORDINATA ACCURATEZZA ENTROPIA
    numeroEsempi = (int) (len(dataset)*percentuale)
    print "NUMERO DATI:"+str(len(dataset))
    print "NUMERO ESEMPI:"+str(numeroEsempi)

    sys.stdout.write("VALIDATION SET")
    sys.stdout.flush()

    # Si inizializzano le variabili
    trainSet = dataset[:]
    validationSet = []
    tmp = []

    # I seguenti cicli permettono di dividere trainset e testset in base a una percentuale
    for i in range(0, numeroEsempi):
        tmp.append(trainSet.pop(0))
    print "##############"
    print "##############"
    print "##############"
    print " LUNGHEZZA TMP:"+str(tmp.__len__())
    for i in range(len(trainSet)):
        validationSet.append(trainSet.pop(0))
    print 'TRAIN SET'
    trainSet.extend(tmp)
    print "Lunghezza TRAIN:"+str(len(trainSet))
    print "##############    TRAIN"
    #print trainSet
    print "##############    FINE TRAIN"
    print "LUNGHEZZA VALIDATION SET:"+str(len(validationSet))
    print "##############    TEST"
    #print validationSet
    print "##############    FINE TEST"
    print "PERCENTUALE DI APPRENDIMENTO:"+str(percentuale*100)+"%"
    # Si crea l'albero di decisione usando il trainset
    albero = creaAlberoDecisione(trainSet, attributi, target, None, pruning)

    # si calcola lo score sul trainset
    score_train = 0.0
    for i in trainSet:
        if getValoreTarget(albero, i) is not None:
            score_train = score_train + 1.0
    score_train = score_train / len(trainSet)
    # Si calcola lo score dell'albero in base ai dati del validation set
    score_validation = 0.0
    for i in validationSet:
        if getValoreTarget(albero, i) is not None:
            score_validation = score_validation + 1.0

    score_validation = score_validation / len(validationSet)
    print
    sys.stdout.write("FINE VALIDATION SET")
    sys.stdout.flush()
    print
    #ritorna l'accuratezza
    return [Decimal(score_train).quantize(Decimal('0.0001')),Decimal(score_validation).quantize(Decimal('0.0001'))]


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
