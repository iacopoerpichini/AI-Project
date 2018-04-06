from random import shuffle


# La funzione ritorna un dataset, una lista di attributi e l'attributo target
# un file csv e la posizione del target all'interno della lista di attributi
def import_dataset_csv(file_name, target_position):
    file = open(file_name, 'r')
    rows = [row.strip() for row in file.readlines()]
    attributes = [attribute.strip() for attribute in rows.pop(0).split(",")]
    target = attributes[target_position - 1] # LA USO PER TRATTARE I VETTORI DA 1 A N
    # Ogni riga sara' quindi un dizionario dove ad ogni attributo viene associato un certo valore
    dataset = []
    for row in rows:
        dataset.append(dict(zip(attributes, [element.strip() for element in row.split(",")])))

    shuffle(dataset)

    file.close()
    return dataset, attributes, target
