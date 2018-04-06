import matplotlib.pyplot as plt

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

def plot_comparation(name, percentages, accuracy, accuracy_pruning):
    plt.plot(percentages, accuracy)
    plt.plot(percentages, accuracy_pruning)
    plt.title("Confronto curve di apprendimento test set di:" + str(name) )
    plt.xlabel("Percentuali apprendimento dataset")
    plt.ylabel("Accuratezza su test set")
    plt.legend(['Accuratezza senza pruning', 'Accuratezza con pruning'])
    plt.show()