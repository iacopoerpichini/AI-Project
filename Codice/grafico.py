import matplotlib.pyplot as plt

def create_plot(name, percentages, accuracy_train, accuracy_validation, pruning):
    plt.plot(percentages, accuracy_train)
    plt.plot(percentages, accuracy_validation)
    if pruning == 0:
        plt.title("Curva di apprendimento " + str(name) + " SENZA pruning")
    elif pruning == 1:
        plt.title("Curva di apprendimento " + str(name) + " CON pruning")
    plt.xlabel("Percentuali apprendimento test set")
    plt.ylabel("Accuratezza su validation set")
    plt.legend(['Accuratezza training', 'Accuratezza validation set'])
    plt.show()

def create_plot_validation(name, percentages, accuracy, accuracy_pruning):
    plt.plot(percentages, accuracy)
    plt.plot(percentages, accuracy_pruning)
    plt.title("Curva di apprendimento di " + str(name) )
    plt.xlabel("Percentuali apprendimento data set")
    plt.ylabel("Accuratezza su validation set")
    plt.legend(['Accuratezza senza pruning', 'Accuratezza con pruning'])
    plt.show()