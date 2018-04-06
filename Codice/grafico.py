import matplotlib.pyplot as plt

#Questa funzione crea un grafico comparando le accuratezze su trainset e test seti di un dataset
def create_plot(name, percentages, accuracy_train, accuracy_validation, pruning):
    plt.plot(percentages, accuracy_train)
    plt.plot(percentages, accuracy_validation)
    if pruning == 0:
        plt.title("Curve di apprendimento " + str(name) + " SENZA pruning")
    elif pruning == 1:
        plt.title("Curve di apprendimento " + str(name) + " CON pruning")
    plt.xlabel("Percentuali apprendimento dataset")
    plt.ylabel("Accuratezza su test set")
    plt.legend(['Accuratezza training set', 'Accuratezza test set'])
    plt.show()

#Questa funzione crea un grafico che compare due curve sul test set
def plot_comparation(name, percentages, frist_cruve, second_curve):
    plt.plot(percentages, frist_cruve)
    plt.plot(percentages, second_curve)
    plt.title("Confronto curve di apprendimento test set di:" + str(name) )
    plt.xlabel("Percentuali apprendimento dataset")
    plt.ylabel("Accuratezza su test set")
    plt.legend(['Accuratezza senza pruning', 'Accuratezza con pruning'])
    plt.show()