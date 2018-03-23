import matplotlib.pyplot as plt

def crea_grafico(percentuali,accuratezza,pruning):
    if pruning == 0:
        print accuratezza
        print "valore accuratezza :" + str(accuratezza)
        print "valore accuratezza pruning:" + str(accuratezza)
        plt.plot(percentuali, accuratezza)
        plt.title("Curva di apprendimento SENZA pruning")
        plt.xlabel("Percentuali apprendimento test set")
        plt.ylabel("Accuratezza su validation set")
        plt.legend(['Accuratezza training', 'Accuratezza validation set'])
        plt.show()
    elif pruning == 1:
        plt.plot(percentuali, accuratezza)
        plt.title("Curva di apprendimento CON pruning")
        plt.xlabel("Percentuali apprendimento test set")
        plt.ylabel("Accuratezza su validation set")
        plt.legend(['Accuratezza training', 'Accuratezza validation set'])
        plt.show()
