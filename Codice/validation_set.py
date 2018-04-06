from albero_di_decisione import *
import fpformat
from random import shuffle

# La funzione divide il dataset in trainset e test set a seconda della percentuale
# passata per parametro la profondita per il pruning viene calcolta dal validation set che e' un sottoinseme del trainset
# mentre il numero di test serve per fare test multipli e calcolare una media di valori
def test(dataset, attributes, target, percentage, num_test, pruning):
    num_examples = (int) (len(dataset) * percentage)
    # Si inizializzano le variabili
    accuracy_train_tot = 0.0
    accuracy_test_tot = 0.0
    # ESEGUO PIU' VOLTE IL TEST PER AVERE RISULTATI PIU' ACCURATI
    for test in range(num_test):
        shuffle(dataset)  # a ogni test si mischia il dataset PER DIFFERENZIARE I TEST
        #DIVIDO IL DATASET IN TRAIN SET (CHE E' DIVISO A SUA VOLTA IN TRAIN E VALIDATION) E TEST SET
        train_set = dataset[:int(num_examples*0.8)]
        validation_set = dataset[int(num_examples * 0.8):int(num_examples)]
        test_set = dataset[int(num_examples):]
        '''
        #VECCHIA VERSIONE DI DIVISIONE DATASET
        # I seguenti cicli permettono di dividere trainset e testset in base a una percentuale
        for i in range(0, num_examples):
            tmp.append(train_set.pop(0))
        for i in range(len(train_set)):
            test_set.append(train_set.pop(0))
        train_set.extend(tmp)
        '''
        best_depth = 100000
        best_score = 0.0
        #SE PRUNING VALE 1 ALLORA UTILIZZO IL VALIDATION SET PER SCEGLIERE IL MIGLIOR PARAMETRO PER PRUNARE L'ALBERO
        #ALTRIMENTI COME PROFONDITA' MASSIMA VIENE PASSATO UN VALORE MOLTO ALTO CHE NON PRUNA L'ALBERO
        if pruning == 1 :
            for depth in range(20) :
                accuracy = 0.0
                for k in range(7): #FACCIO UNA MEDIA TRA 5 TEST PER SCEGLIERE L'ACCURATEZZA E LA PRONDITA' MIGLIORI PER PRUNARE
                    tree = create_decision_tree(train_set, attributes, target, None, depth)
                    for i in validation_set :
                        if get_target_value(tree, i) == i[target] :
                            accuracy = accuracy + 1.0
                accuracy /= len(validation_set) * 7
                if best_score < accuracy :
                    best_score = accuracy
                    best_depth = depth
                else :
                    break
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
        print "LUNGHEZZA VALIDATION SET:"+str(len(test_set))
        print "##############    TEST"
        #print test_set
        print "##############    FINE TEST"
        print "PERCENTUALE DI APPRENDIMENTO:"+str(percentuale*100)+"%"
        #HA SENSO RIMISCHIARE I DATI?!?!?!
        # shuffle(albero)
        # print albero
        #stampa_albero(albero,"") #FUNZIONE USATA PER VEDERE l'ALBERO SU ESEMPI SEMPLICI
        '''
        # Si calcola lo score dell'albero in base ai dati presenti nel TRAIN SET UNITO AL VALIDATION SET
        train_set.extend(validation_set)
        #IN TREE E' PRESENTE IL CLASSIFICATORE CHE HO UTILIZZATO
        tree = create_decision_tree(train_set, attributes, target, None, best_depth)
        #print_tree(tree,"") #debug
        accuracy_train = 0.0
        accuracy_test = 0.0
        for i in train_set:
            if get_target_value(tree, i) == i[target]:
                accuracy_train = accuracy_train + 1.0
        accuracy_train_tot = accuracy_train_tot + (accuracy_train / len(train_set))
        # Si calcola lo score dell'albero in base ai dati presenti nel TEST SET
        for i in test_set:
            if get_target_value(tree, i) == i[target]:
                accuracy_test = accuracy_test + 1.0
        accuracy_test_tot = accuracy_test_tot + (accuracy_test / len(test_set))
        # ritorna l'accuratezza SUL TRAIN(TRAIN+VALIDATION) E SUL TEST
    return [fpformat.fix(accuracy_train_tot / num_test, 8), fpformat.fix(accuracy_test_tot / num_test, 8)]

#Questa funzione mi serve per eseguire il confronto sulle predizioni dell' accuratezza dell'albero
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
