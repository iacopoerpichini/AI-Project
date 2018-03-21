from importa_file import *
from albero_di_decisione import *
import time
from decimal import *
import matplotlib.pyplot as plt


ctx = localcontext()
ctx.rounding = ROUND_DOWN


def validation_set(dataset, attributi, target, percentuale,pruning):
    #SCRIVERE L'ALG DI APPRENDIMENTO ALBERI CON E SENZA PRUNING
    #A SECONDA DEL VALORE CHE PASSERO' PER PARAMETRO
    if pruning == False :
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
    time.sleep(0.15)

    # Si inizializzano le variabili
    score = 0.0
    trainSet = dataset[:]
    validationSet = []
    tmp = []

    # I seguenti cicli permettono di non avere mai train e test uguali
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
    print trainSet
    print "##############    FINE TRAIN"
    print "LUNGHEZZA VALIDATION SET:"+str(len(validationSet))
    print "##############    TEST"
    print validationSet
    print "##############    FINE TEST"
    # Si crea l'albero di decisione usando il trainset
    albero = creaAlberoDecisione(trainSet, attributi, target, None, pruning)

    # Si calcola lo score dell'albero in base ai dati del validation set

    for i in validationSet:
        if getValoreTarget(albero, i) is not None:
            score = score + 1.0

    score = score / len(validationSet)
    print
    sys.stdout.write("FINE VALIDATION SET")
    sys.stdout.flush()

    print
    return Decimal(score).quantize(Decimal('0.00001'))


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


def mainFunction():
    dataSets = ["carClassifier.csv","uci-20070111-page-blocks.csv","australian.csv"]
    posizione_target = [5,1,14]

    #dataSets = ["australian.csv"]
    #posizione_target = [11]
    for i in range(0, dataSets.__len__()) :
        dataset, attributi, target = importa_dataset_csv(dataSets[i], posizione_target[i])

        '''
        print "-------inizio dataset-----"
        print dataset
        print "------------"
        print attributi
        print "------------"
        print target
        print "------------"
        print "------------"
        print "------------" 
        '''

        entropia = []
        percentuali = [0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95]
        #percentuali = [0.7]
        for i in range(0,len(percentuali)) :
            tmp = validation_set(dataset, attributi, target, percentuali[i],0)#false sta per pruning si o no
            entropia.append(tmp)
            #70 trainset e 30 testset
        print "valore correttezza:" + str(entropia)

        plt.plot(percentuali, entropia)
        plt.title("Curva di apprendimento")
        plt.xlabel("Percentuali apprendimento test set")
        plt.ylabel("Accuratezza su validation set")
        plt.show()


if __name__ == "__main__":
    mainFunction()

