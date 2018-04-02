from importa_file import importa_dataset_csv
from validation_set import *
from grafico import *
from timeit import default_timer as timer
import fpformat
import sys

def main():
    #INIZIALIZZAZIONI VARIABILI
    percentages = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    data_sets = ["breast-cancer-wisconsin.csv","carClassifier.csv","contraceptive.csv","balance-scale.csv","agaricus-lepiota.csv"]
    target_positions = [11, 2, 10, 1, 23]
    #Parametro per il pruning
    depth = [2, 7, 5, 8, 8]
    min_sample_leaf = [1, 1, 1, 2, 1]
    #Parametro per eseguire test multipli e migliorare l'accuratezza
    num_test = [2, 4, 4, 20, 2]
    for j in range(len(data_sets)) :
        dataset, attributes, target = importa_dataset_csv(data_sets[j], target_positions[j])
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
        accuracy_train = []
        accuracy_validation = []
        accuracy_pruning_train = []
        accuracy_pruning_validation = []
        time = []
        pruning_time = []
        for i in range(0,len(percentages)) :
            sys.stdout.write("\r{0}".format("Analisi dataset:\"" + str(data_sets[j]) + "\", Percentuale training:" + str(percentages[i] * 100) + "%"))
            sys.stdout.flush()
            start = timer()
            tmp = validation_set(dataset, attributes, target, percentages[i], 99999, 1, num_test[j])  # 9999 di profondita non pruna
            end = timer()
            accuracy_train.append(tmp[0])
            accuracy_validation.append(tmp[1])
            time.append(fpformat.fix((end - start),4))
            #TEST PRUNING
            start = timer()
            tmp_pruning = validation_set(dataset, attributes, target, percentages[i], depth[j], min_sample_leaf[j], num_test[j]) # pruna secondo una profondita
            end = timer()
            accuracy_pruning_train.append(tmp_pruning[0])
            accuracy_pruning_validation.append(tmp_pruning[1])
            pruning_time.append(fpformat.fix((end - start),4))
        #OUTPUT PROGRAMMA
        create_plot(data_sets[j], percentages, accuracy_train, accuracy_validation, 0)
        create_plot(data_sets[j], percentages, accuracy_pruning_train, accuracy_pruning_validation, 1)
        create_plot_validation(data_sets[j], percentages, accuracy_validation, accuracy_pruning_validation)
        print "\nTempi esecuzione validation set senza pruning:" + str(time) + " con numero di test:" +str(num_test[j])
        print "Tempi esecuzione validation set con pruning:" + str(pruning_time) + " con numero di test:" +str(num_test[j])
        print "Percentuali di apprendimento:" + str(percentages)
        print "Accuratezza senza pruning:" + str(accuracy_validation)
        print "Accuratezza con pruning:" + str(accuracy_pruning_validation)
        #MANCA LOUTPUT DEI DATI
        #print "I valori dell'accuratezza riguardano l'accuratezza sul training set e sul validation set. es. [[train,validation],...] in base alla percentuale di apprendimento"
        #print "Valori accuratezza:" + str(accuracy)
        #print "Valori accuratezza applicando pruning:" + str(accuracy_pruning)


if __name__ == "__main__":
    main()
