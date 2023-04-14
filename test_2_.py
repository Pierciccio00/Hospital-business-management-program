    from PAZIENTI_PIERFRANCESCO_LINDIA_213125 import Ricovero
from test_1 import *
import datetime
import numpy as np
import pandas as pd

### N.B
###   L'INTERO PROGRAMMA E' STATO APPOSITAMENTE CREATO ,SEGUENDO LE RICHIESTE IN TRACCIA, AL FINE DI RESTITUIRE INFORMAZIONI SULLA BASE DI FUTURI INSERIMENTI , IMPLEMENTAZIONI 
###   O MODIFICHE DEL FILE TXT. 
###   IN PARTICOLARE,DA NOTARE LA FUNZIONE (numero_ricoveri_per_regione) CHE CREARE IL DIZIONARIO, FUNZIONE PER IL CALCOLO DELLA MEDIANA SIA CON PANDAS CHE CON L'UTILIZZO DEL DIZIONARIO.
###



#### MEDIANA == > IMPLEMENTO ENTRAMBI I METODI PERCHE' INIZIALMENTE NON RIUSCENDO A CALCOLARE LA MEDIANA ATTRAVERSO L'UTILIZZO DI LISTE, AVEVO OPTATO PER L'UTILIZZO DELLA LIBRERIA PANDAS,
####              MENTRO IMPLEMENTAVO L'ULTIMA FUNZIONE CON IL DIZIONARIO, HO AVUTO L'IDEA DI FAR SCORRERE UN DIZIONARIO PER CREARE LA LISTA, CHE MI E' SERVITA PER DETERMINARE LA MEDIANA.





    
def numero_ricoveri_per_regione(lista):
    a=datetime.datetime.strptime("01/01/2020", "%d/%m/%Y" )
    b=datetime.datetime.strptime("31/12/2020", "%d/%m/%Y" ) 
    diz={}
    for i in range(len(lista)):
        if lista[i].get_regione_di_residenza() not in diz and (3<=lista[i].get_numero_giorni_degenza()<=5) and a<=lista[i].get_data_inizio_ricovero()<=b:
            diz[lista[i].get_regione_di_residenza()]=1
        elif lista[i].get_regione_di_residenza() in diz and (3<=lista[i].get_numero_giorni_degenza()<=5) and a<=lista[i].get_data_inizio_ricovero()<=b:
            diz[lista[i].get_regione_di_residenza()]+=1
            
    return diz
    
    

def mediana_con_pandas(lista):
    a=datetime.datetime.strptime("01/01/2020", "%d/%m/%Y" )
    b=datetime.datetime.strptime("31/12/2020", "%d/%m/%Y" )     
    numero_giorni_degenza = []
    for i in range(len(lista)):
        if a<=lista[i].get_data_inizio_ricovero()<=b:
            numero_giorni_degenza.append(lista[i].get_numero_giorni_degenza())
            numero_giorni_degenza.sort()
    df = pd.DataFrame(data=numero_giorni_degenza, columns = ["MEDIANA = "])
    median=df.median(skipna=None)
    return numero_giorni_degenza, median



def mediana_con_dizionario(lista):
    dizionario={}
    a=datetime.datetime.strptime("01/01/2020", "%d/%m/%Y" )
    b=datetime.datetime.strptime("31/12/2020", "%d/%m/%Y" )  
    lista_1=[]
    mediana=0
    for i in range(len(lista)):
        if a<=lista[i].get_data_inizio_ricovero()<=b:
            dizionario[lista[i].get_id_ricovero]=lista[i].get_numero_giorni_degenza()
    for i in dizionario:
        lista_1.append(dizionario[i])
    lista_1.sort()
    if len(lista_1)%2==0:
        mediana=lista_1[len(lista_1)%2]
    else:
        mediana=lista_1[(len(lista_1)%2)+(len(lista_1)%2)+1]
    return print(lista_1, "MEDIANA =", mediana) 
        
    
def percentuale(lista):
    denominatore=0
    numeratore=0
    ## UTILIZZO LE FUNZIONALITA' DI DATETIME PER OTTENERE IL RANGE DESIDERATO.
    a=datetime.datetime.strptime("01/01/2021", "%d/%m/%Y" )
    b=datetime.datetime.strptime("31/12/2021", "%d/%m/%Y" )
    for i in range(len(lista)):
        if a<=lista[i].get_data_inizio_ricovero()<=b:
            denominatore+=1
    for i in range(len(lista)):
        if (lista[i].get_patologie_respiratorie()== True or lista[i].get_patologie_cardiache()== True) and a<=lista[i].get_data_inizio_ricovero()<=b:
            numeratore+=1
    percentuale=(numeratore/denominatore)*100
    return percentuale


def Pandas(lista):
    Codice_fiscale = []
    numero_giorni_degenza = []
    esito_tampone_covid=[]
    for i in lista:
        Codice_fiscale.append(i.get_cod_fiscale())
        numero_giorni_degenza.append(i.get_numero_giorni_degenza())
        esito_tampone_covid.append(i.get_esito_tampone_covid())
    ## CREO IL DATAFRAME 
    dataframe = pd.DataFrame(data=Codice_fiscale, columns = ["Codice fiscale"])
    dataframe["GIORNI DEGENZA"] = numero_giorni_degenza
    dataframe["COVID"]= esito_tampone_covid
    result = dataframe[(dataframe["GIORNI DEGENZA"] > 10) & (dataframe["COVID"] == "POSITIVO")]
    return result
    



def main():
    ricoveri_ordinati=[]
    #apro il file in lettura
    try:
        inputFile = open("PAZIENTI.txt","r")
    except IOError as e:
        print("ERRORE:Impossibile aprire il file")
        exit()
    line=inputFile.readline()
    while line != "":
        scheda=Ricovero.fromString(line)
        ricoveri_ordinati.append(scheda)
        #leggo il contenuto di ogni riga
        line= inputFile.readline()   
        Ricovero.numero_giorni_degenza(scheda)
        Ricovero.calcola_costo_Prestazione_Sanitaria(scheda)
        
    # INSIEME DI SCHEDE RICOVERO ORDINATI
        ricoveri_ordinati.sort()
        salvainfile(ricoveri_ordinati)  
    print("000000000000000000000000 SCHEDE RICOVERO ORDINATE 0000000000000000000000000000000000000000") 
    print()
    inputFile.close()
    for j in ricoveri_ordinati:
        print(j) 
        
        
        
        

    ###########  PERCENTUALE DEI RICOVERI ##########################
    print("LA PERCENTUALE E DEL :",percentuale(ricoveri_ordinati),"%")
    print()
    
    ############ CODICI FISCALI DEI PAZIENTI CALABRESI AFFETTI DA COVID CON UN NUMERO DI GIORNI DI DEGENZA > 10 ################################
    print("########################")
    ############ UTILIZZANDO LA LIBRERIA PANDAS
    print(Pandas(ricoveri_ordinati))
    print()
    
    print("########################")
    ########### MEDIANA CON PANDAS ###########
    print(mediana_con_pandas(ricoveri_ordinati))
    print()
    
    
    ################# PER OGNI REGIONE DI RESIDENZA IL NUMERO DI RICOVERI EFFETTUATI NEL 2020 CON NUMERO GIORNI DEGENZA COMPRESI TRA 3 E 5 INCLUSI ###########################
    print("#################################")
    print(numero_ricoveri_per_regione(ricoveri_ordinati))
    print()

    
    ######### MEDIANA CALCOLATA CON IL DIZIONARIO ################################
    print("###################")
    print()
    print(mediana_con_dizionario(ricoveri_ordinati))
main()