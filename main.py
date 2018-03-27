from importa_file import importa_dataset_csv
from validation_set import validation_set
from grafico import crea_grafico
from timeit import default_timer as timer
import fpformat

def main():
    #INIZIALIZZAZIONI VARIABILI
    percentuali = [0.01, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9,0.95, 0.99]
    data_sets = ["balance-scale.csv","carClassifier.csv","agaricus-lepiota.csv"]
    posizione_target = [1,1,22]
    profondita = [1, 3, 3]
    num_test = [15, 10, 3]

    for j in range(0, data_sets.__len__()) :
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
            start = timer()
            tmp = validation_set(dataset, attributi, target, percentuali[i], 99999, num_test[j])  # 9999 di profondita non pruna
            accuratezza.append(tmp)
            print tmp
            end = timer()
            tempo.append(fpformat.fix((end - start),4))
            #TEST PRUNING
            start = timer()
            tmp_pruning = validation_set(dataset, attributi, target, percentuali[i], profondita[j], num_test[j]) # pruna secondo una profondita
            accuratezza_pruning.append(tmp_pruning)
            end = timer()
            tempo_pruning.append(fpformat.fix((end - start),4))

        crea_grafico(percentuali,accuratezza,0)
        crea_grafico(percentuali,accuratezza_pruning,1)
        print "tempo validation set senza pruning in base alle percentuali di train e test :" + str(tempo)
        print "tempo validation set con pruning in base alle percentuali di train e test :" + str(tempo_pruning)
        print "percentuali di apprendimento :" + str(percentuali)
        print "valore accuratezza :" + str(accuratezza)
        print "valore accuratezza pruning:" + str(accuratezza_pruning)

if __name__ == "__main__":
    main()

