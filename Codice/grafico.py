import matplotlib.pyplot as plt

def crea_grafico(nome,percentuali,accuratezza,pruning):
    plt.plot(percentuali, accuratezza)
    if pruning == 0:
        plt.title("Curva di apprendimento "+ str(nome) +" SENZA pruning")
    elif pruning == 1:
        plt.title("Curva di apprendimento "+ str(nome) +" CON pruning")
    plt.xlabel("Percentuali apprendimento test set")
    plt.ylabel("Accuratezza su validation set")
    plt.legend(['Accuratezza training', 'Accuratezza validation set'])
    plt.show()