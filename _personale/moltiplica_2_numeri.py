import sys

#print(sys.argv)
#stampa gli argomenti del programma che è python
#lista degli argomenti che abbiamo passato quando abbiamo lanciato l'interprete
#il primo argomento è sempre il nome dello script
#devo fare dei controlli
if len(sys.argv) != 3:
    print('Il numero di parametri passati non è corretto. Devi inserire due numeri')
else:
    try:
        primo_numero = float(sys.argv[1])
    except ValueError: #avrei potuto usare il generico Exception
        print('Hai inserito un valore che non può essere convertito in float:', sys.argv[1])
    try:
        secondo_numero = float(sys.argv[2])
    except ValueError: #avrei potuto usare il generico Exception
        print('Hai inserito un valore che non può essere convertito in float:', sys.argv[2])
    risultato = primo_numero * secondo_numero

print(f'Il risultato di {primo_numero} per {secondo_numero} è uguale a {risultato}')


#gli argomenti sono sotto forma di stringa
#gli errori sono degli oggetti, python prende la classe degli errori, istanzia la classe 