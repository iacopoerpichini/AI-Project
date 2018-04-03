from importa_file import importa_dataset_csv
from validation_set import *
from grafico import *
from timeit import default_timer as timer
import fpformat
import sys

#INIZIALIZZAZIONI VARIABILI
percentages = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
data_sets = ["votes.csv", "car-classifier.csv", "contraceptive.csv"]
target_positions = [17, 7, 10]
#Parametro per eseguire test multipli e migliorare l'accuratezza
num_test = [90, 50, 60]

def main():
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
            #TEST SENZA PRUNING
            start = timer()
            tmp = test(dataset, attributes, target, percentages[i], num_test[j], 0)  #0 sta per senza pruning
            end = timer()
            accuracy_train.append(tmp[0])
            accuracy_validation.append(tmp[1])
            time.append(fpformat.fix((end - start),4))

            #TEST PRUNING
            start = timer()
            tmp_pruning = test(dataset, attributes, target, percentages[i], num_test[j], 1) #1 sta per pruning
            end = timer()
            accuracy_pruning_train.append(tmp_pruning[0])
            accuracy_pruning_validation.append(tmp_pruning[1])
            pruning_time.append(fpformat.fix((end - start),4))

        #OUTPUT PROGRAMMA
        create_plot(data_sets[j], percentages, accuracy_train, accuracy_validation, 0)
        create_plot(data_sets[j], percentages, accuracy_pruning_train, accuracy_pruning_validation, 1)
        plot_comparation(data_sets[j], percentages, accuracy_validation, accuracy_pruning_validation)
        print " con numero di test per percentuale = " + str(num_test[j])
        print "Tempi esecuzione senza pruning:" + str(time)
        print "Tempi esecuzione con pruning:" + str(pruning_time)
        print "Percentuali di apprendimento:" + str(percentages)
        print "Accuratezza senza pruning:" + str(accuracy_validation)
        print "Accuratezza con pruning:" + str(accuracy_pruning_validation)


if __name__ == "__main__":
    main()
