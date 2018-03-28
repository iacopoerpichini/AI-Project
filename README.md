
Guida installazione
=======

Per far funzionare il programma basta semplicemente scaricarlo e eseguirlo, al suo interno sono già presenti tre data set su cui vengono eseguite delle prove.

Per modificare i parametri basta modificare il file "main.py" nella sezione inizializzazioni variabili.

Variabili dell'ambiente :
1. percentuali = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9] : Sono le percentuali su cui viene eseguito il validationset per descrivere la curva di apprendimento dell' albero decisionale.
2. data_sets = ["contraceptive.csv","balance-scale.csv","agaricus-lepiota.csv"] : La lista dei dataset testati.
3. posizione_target = [10, 1, 23] : La posizione dei target relativi ai dataset sopra citati.
4. profondita = [5, 8, 3] : Parametro utilizzato per il pruning nei vari test.
5. min_foglie_campione = [1, 2, 1]: Parametro utilizzato per il pruning nei vari test.
6. num_test = [5, 15, 3] : Numero di test ripetuti per disegnare curve meno oscillanti.

I miei test fanno riferimento alle variabili riportate qui sopra.

Devo fare alcune osservazioni:
* Se vogliamo aggiungere un nuovo dataset deve essere messo nella cartella contenente il programma python

* I dataset devono contenere come prima riga la lista degli attributi.

* Dobbiamo scegliere con criterio la posizione del target di ogni dataset contando che i numeri vanno da 1...N

Riferimenti
-----------

Il seguente [Articolo](http://archive.oreilly.com/pub/a/python/2006/02/09/ai_decision_trees.html) mi ha aiutato a capire a fondo gli alberi decisionali e a implementare l'algoritmo id3.

Mentre il seguente [Articolo](https://triangleinequality.wordpress.com/2013/09/01/decision-trees-part-3-pruning-your-tree/) mi è servito per capire a fondo il pruning per poi poterlo implementare.

In linea generale ho utilizzato anche [Mitchell cap.3](https://github.com/iacopoerpichini/AI-Project/blob/master/Mitchell%20cap.3.pdf) per lo studio dell' argomento in analisi.

