#aprire il file
import os
import json
#ascii sta per american standard etc. allora bisogna dire che il set di caratteri da usare è utf-8
nome_file = 'dati_di_base.csv'
nome_file = os.path.abspath(nome_file)
with open('_personale/lezione_23_04/dati_di_base.csv', 'r', encoding='utf-8') as fr:
    
#leggere il file
    paperino = fr.read()

#dividere per righe
    righe = paperino.split('\n')

#costruire il dizionario
    dizdati = {}

#dividere ogni riga per colonna = creo delle liste in pratica
    riga = 0

    for r in righe:
        lista = r.split(';')

        #print(r)
        print("1",lista)

        if riga == 0:
            chiavi = lista
            #accedo alla prima riga, la lista che ha le intestazioni e la salvo in una variabile a parte "chiavi"
            #su cui non ritornerò

        else:
            dizdati[riga] = {} #ho costruio un dizionario e ora lo sto annidando
            dizdati[riga][chiavi[0]] = lista[0] #occhio che questo è il primo elemento (index 0) della lista "chiavi" =! dalla lista alla riga 0
            #quindi è una stringa, cioè "nome"
            dizdati[riga][chiavi[1]] = lista[1]
            dizdati[riga][chiavi[2]] = lista[2]

        riga = riga + 1

    print( "questo è il dizionario annidato alla fine del ciclo for", dizdati)

#convertire il dizionario in json
    jdata = json.dumps(dizdati)

    print('JSON ->', jdata)
    print('DIZIONARIO ->', dizdati)

#scrivere dati in formato json
    with open('_personale/lezione_23_04/jdati_di_base.json', 'w', encoding='utf-8') as fw:
        fw.write(jdata)

#adesso dobbiamo fare il contrario

#leggo il file .json
    with open('_personale/lezione_23_04/jdati_di_base.json', 'r', encoding='utf-8') as fr:
        buffer = fr.read()

#lo ritrasformo in un dizionario
    dicDatiNew = json.loads(buffer)
    print(dicDatiNew)


#rifaccio il file .csv
    #devo ottenere l'elenco delle chiavi del dizionario
    chiavi = dicDatiNew.keys()
    print("queste invece sono le chiavi", chiavi)

    righe = 0
    
    file = []

    for k in chiavi:
        dicPiccolo = dicDatiNew[k]
        #costruire il nome della chiave
        chiaviCSV = dicPiccolo.keys()
        rigaCSV = ''
        if righe == 0:
            #prima riga del file csv
            rigaIntestazione = ''
            for k2 in chiaviCSV:
                rigaIntestazione += k2 + ';'
            print(rigaIntestazione)
            intestazione = rigaIntestazione[:-1]
            intestazione = intestazione + '\n'
        
            file.append(intestazione)

            righe += 1
        else:
            
            for k3 in chiaviCSV:
                rigaCSV += dicPiccolo[k3] + ';' #prendo i dati del dizionario = i valori, values
            rigaCSV = rigaCSV[:-1] + '\n'

            file.append(rigaCSV)
            print(rigaCSV)
    print(file)   

    #devo scrivere il nuovo file csv
    buffer = ''
    for z in file:
        buffer += z

    buffer = buffer[:-1]
    with open('_personale/lezione_23_04/nuovocsv.CSV', 'w', encoding='utf-8') as fw:
            fw.write(buffer)