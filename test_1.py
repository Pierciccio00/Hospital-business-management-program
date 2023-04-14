from PAZIENTI_PIERFRANCESCO_LINDIA_213125 import Ricovero
import datetime

#creo una lista vuota
def salvainfile(a):
    #apro file in output modalita scrittura
    fileoutput = open("PAZIENTI.txt", "w")
    
    for i in range(len(a)):
        #formatto le date 
        Data_formattata_1 = (a[i].get_data_inizio_ricovero())
        Data_formattata_2 = (a[i].get_data_fine_ricovero())
        stringa_concatenata=a[i].get_id_ricovero()+ ":" +a[i].get_cod_fiscale()+ ":" +a[i].get_nome() + ":" +a[i].get_cognome() + ":" +a[i].get_regione_di_residenza()+ ":" +str(Data_formattata_1) + \
        " " +str(Data_formattata_2)+ ":"+ str(a[i].get_patologie_cardiache())+ ":" + str(a[i].get_patologie_respiratorie())+ ":" + a[i].get_esito_tampone_covid() + ":" + a[i].get_diagnosi()
        
        #scrivo una riga del file con questa stringa 
        fileoutput.write(stringa_concatenata+"\n")
    #chiudo il file
    fileoutput.close()  


def main():
 
    ricoveri=[]
    #apro il file in lettura
    try:
        inputFile = open("PAZIENTI.txt","r")
    except IOError as e:
        print("ERRORE:Impossibile aprire il file")
        exit()

    line=inputFile.readline()
    while line != "":
        #creo il paziente
        scheda=Ricovero.fromString(line)
       

        #aggiungo alla lista pazienti il paziente
        ricoveri.append(scheda)
        #leggo il contenuto di ogni riga
        line= inputFile.readline()
        #RICHIAMO LA FUNZIONE PER IL CALCOLO DEL NUMERO DEI GIORNI DI DEGENZA PER OGNI PAZIENTE
        Ricovero.numero_giorni_degenza(scheda)
        #RICHIAMO LA FUNZIONE PER IL CALCOLO DEL COSTO DELLE PRESTAZIONI FINANZIARIE
        Ricovero.calcola_costo_Prestazione_Sanitaria(scheda)
        
        
       
        
    inputFile.close()
    for i in ricoveri:
        print(i)

    

        
        
        
        
 
main()





