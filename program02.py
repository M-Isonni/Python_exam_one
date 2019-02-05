'''
Abbiamo n pulsanti numerati da 1 a N ed N lampadine anch'esse numerate da 1 a N.
Il generico pulsante x cambia lo stato (da accesa a spenta o viceversa) della lampadina x
e di tutte le lampadine il cui numero identificativo e' un divisore di x.
Ad esempio il pulsante 18 cambia lo stato delle lampadine 1,2,3,6,9,18.
Ogni pulsante puo' essere premuto al massimo una volta e i pulsanti vanno premuti
in ordine crescente (una volta premuto il pulsante x  non e' piu' possibile premere
i pulsanti da 1 a x-1).
Sapendo N e l'insieme 'accese' delle lampadine al momento accese
bisogna individuare la sequenza crescente di bottoni da premere perche'
tutte le lampadine risultino accese.
Definire una funzione es2(N, accese) che dati:
- il numero N di lampadine
- l'insieme 'accese' contenente gli identificativi delle lampadine al momento accese
determina e restituisce la lista contenente nell'ordine i pulsanti da premere perche'
le N lampadine risultino tutte accese.
Ad esempio per N=6 e accese={2,4} es2(N, accese) restituisce la lista [2,5,6] infatti:
-all'inizio sono accese le lampadine {2,4}
-dopo aver premuto il pulsante 2 saranno accese le lampadine {1,4}
-dopo aver premuto il pulsante 5 saranno accese le lampadine {4,5}
-dopo aver premuto il pulsante 6 saranno accese le lampadine {1,2,3,4,5,6}

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
'''


def es2(N:int, ins:list):     
    order_list=[]
    to_avoid =[]     
    while len(ins)<N:
        order_list.clear() 
        my_temp_list = ins.copy()
        for i in range(1,N+1):
            if i in to_avoid:
                continue
            else:
                for j in range(1,i+1):
                    if i%j == 0:
                        if j in my_temp_list:
                            my_temp_list.remove(j)
                        else:
                            my_temp_list.append(j)
            order_list.append(i)
        if len(my_temp_list)<N:
            for i in range(1,N+1):
                if i not in my_temp_list:
                    if i in to_avoid:
                        to_avoid.remove(i)
                    else:
                        to_avoid.append(i) 
        else:
            ins = my_temp_list.copy()
            return order_list
    pass

my_list = [1,3,5,6,9]
N=25
print(es2(N,my_list))
                               
    
