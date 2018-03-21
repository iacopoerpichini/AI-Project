
from random import shuffle

def importa_dataset_csv(nome_file, posizione_target):
    # La funzione ritorna un dataset, una lista di attributi e l'attributo target
    # un file csv (comma separeted values) e la posizione del target all'interno della lista di attributi
    file = open(nome_file, 'r')
    righe = [riga.strip() for riga in file.readlines()]

    attributi = [attribute.strip() for attribute in righe.pop(0).split(",")]
    target = attributi[posizione_target - 1] #LA USO PER TRATTARE I VETTORI DA 1 A N

    # Viene creata una lista di dizionario. Ogni riga sara' quindi un dizionario dove ad ogni attributo
    # sara' associato un certo valore
    dataset = []
    for riga in righe:
        dataset.append(dict(zip(attributi, [element.strip() for element in riga.split(",")])))

    #MISCHIARE IL DATASET e' UTILE PER IL MIO PROGETTO ??!??!?!?!?
    shuffle(dataset)


    file.close()
    return dataset, attributi, target
