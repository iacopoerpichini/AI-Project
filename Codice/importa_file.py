from random import shuffle

def import_dataset_csv(file_name, target_position):
    # La funzione ritorna un dataset, una lista di attributi e l'attributo target
    # un file csv (comma separeted values) e la posizione del target all'interno della lista di attributi
    file = open(file_name, 'r')
    rows = [row.strip() for row in file.readlines()]
    attributes = [attribute.strip() for attribute in rows.pop(0).split(",")]
    target = attributes[target_position - 1] #LA USO PER TRATTARE I VETTORI DA 1 A N
    # Viene creata una lista di dizionario. Ogni riga sara' quindi un dizionario dove ad ogni attributo
    # sara' associato un certo valore
    dataset = []
    for row in rows:
        dataset.append(dict(zip(attributes, [element.strip() for element in row.split(",")])))

    shuffle(dataset)

    file.close()
    return dataset, attributes, target
