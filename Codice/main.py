from importa_file import importa_dataset_csv
from validation_set import validation_set
from grafico import crea_grafico
from timeit import default_timer as timer
import fpformat
import sys

def main():
    #INIZIALIZZAZIONI VARIABILI
    percentuali = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    data_sets = ["contraceptive.csv","balance-scale.csv","agaricus-lepiota.csv"]
    posizione_target = [10, 1, 23]
    profondita = [5, 8, 3]
    min_foglie_campione = [1, 2, 1]
    num_test = [5, 15, 3]

    for j in range(len(data_sets)) :
        dataset, attributi, target = importa_dataset_csv(data_sets[j], posizione_target[j])

        '''
        print "-------inizio dataset-----"
        print dataset
        print "------------"
        print attributi
        print "------------"
        print target
        print "------------"
        '''

        start = timer()
        end = timer()
        print (end - start)
        accuratezza = []
        accuratezza_pruning = []
        tempo = []
        tempo_pruning = []
        for i in range(0,len(percentuali)) :
            sys.stdout.write("\r{0}".format("Analisi dataset numero: " + str(j+1) + ",Percentuale training:" + str(percentuali[i] * 100) + "%"))
            sys.stdout.flush()
            start = timer()
            tmp = validation_set(dataset, attributi, target, percentuali[i], 99999, 1, num_test[j])  # 9999 di profondita non pruna
            accuratezza.append(tmp)
            #print tmp
            end = timer()
            tempo.append(fpformat.fix((end - start),4))
            #TEST PRUNING
            start = timer()
            tmp_pruning = validation_set(dataset, attributi, target, percentuali[i], profondita[j], min_foglie_campione[j], num_test[j]) # pruna secondo una profondita
            accuratezza_pruning.append(tmp_pruning)
            end = timer()
            tempo_pruning.append(fpformat.fix((end - start),4))

        crea_grafico(data_sets[j],percentuali,accuratezza,0)
        crea_grafico(data_sets[j],percentuali,accuratezza_pruning,1)

        print "\nTempi esecuzione validation set senza pruning:" + str(tempo) + " con numero di test:" +str(num_test[j])
        print "Tempi esecuzione validation set con pruning:" + str(tempo_pruning) + " con numero di test:" +str(num_test[j])
        print "Percentuali di apprendimento:" + str(percentuali)
        print "I valori dell'accuratezza riguardano l'accuratezza sul training set e sul validation set. es. [[train,validation],...] in base alla percentuale di apprendimento"
        print "Valori accuratezza:" + str(accuratezza)
        print "Valori accuratezza applicando pruning:" + str(accuratezza_pruning)

if __name__ == "__main__":
    main()

