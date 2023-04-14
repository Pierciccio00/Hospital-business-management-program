#IMPORTO datetime PER LA MANIPOLAZIONE E LA GESTIONE DI DATE 
import datetime 
#import numpy as np
#import pandas as pd

#CREO UNA CLASSE DENNOMINATA RICOVERO, CAPACE DI GESTIRE I DATI RELATIVI AL RICOVERO EFFETUATO DA UN PAZIENTE NELLA STRUTTURA, INSERENDO DIVERSI ATTRIBUTI.
class Ricovero:
    def __init__(self, id_ricovero, cod_fiscale, nome, cognome, regione_di_residenza, data_inizio_ricovero, data_fine_ricovero, patologie_cardiache, patologie_respiratorie, esito_tampone_covid, tipologia_ricovero, diagnosi):
        self.id_ricovero=id_ricovero
        self.cod_fiscale=cod_fiscale
        self.nome=nome
        self.cognome=cognome
        self.regione_di_residenza=regione_di_residenza
        self.data_inizio_ricovero=datetime.datetime.strptime(data_inizio_ricovero, "%d/%m/%Y")
        self.data_fine_ricovero=datetime.datetime.strptime(data_fine_ricovero, "%d/%m/%Y")
        self.patologie_cardiache=bool(patologie_cardiache)
        self.patologie_respiratorie=bool(patologie_respiratorie)
        self.esito_tampone_covid=esito_tampone_covid
        self.tipologia_ricovero=tipologia_ricovero
        self.diagnosi=diagnosi
        self.numero_giorni_degenza=0
        self.costo_totale=0
        self.numero_ricoveri=0
        
    
    ################################################################################################################################
    #IMPLEMENTIAMO IL METODO BUILT-IN __str__ CHE SERVE A TRASFORMARE UN OGGETTO IN UNA STRINGA.
    def __str__(self):
        return f'SCHEDA RICOVERO\nCodice Identificativo:{self.id_ricovero}\nCodice Fiscale:{self.cod_fiscale}\nNome:{self.nome}\nCognome:{self.cognome}\nRegione di Residenza:{self.regione_di_residenza}\nData Inizio ricovero:{str(self.data_inizio_ricovero)}\nData fine Ricovero:{str(self.data_fine_ricovero)}\nPatologie Cardiache:{self.patologie_cardiache}\nPatologie Respiratorie :{self.patologie_respiratorie}\nEsito campione COVID:{self.esito_tampone_covid}\nTipologia Ricovero:{self.tipologia_ricovero}\nDiagnosi Ricovero:{self.diagnosi}\nGiorni Degenza :{self.numero_giorni_degenza}\nCosto Totale:{self.costo_totale}\n\n'
    
    
    #BLOCCO GET
    def get_id_ricovero(self):
        return self.id_ricovero
    def get_cod_fiscale(self):
        return self.cod_fiscale
    def get_nome(self):
        return self.nome
    def get_cognome(self):
        return self.cognome
    def get_regione_di_residenza(self):
        return self.regione_di_residenza
    def get_data_inizio_ricovero(self):
        return self.data_inizio_ricovero
    def get_data_fine_ricovero(self):
        return self.data_fine_ricovero    
    def get_patologie_cardiache(self):
        return self.patologie_cardiache
    def get_patologie_respiratorie(self):
        return self.patologie_respiratorie
    def get_esito_tampone_covid(self):
        return self.esito_tampone_covid    
    def get_tipologia_ricovero(self):
        return self.tipologia_ricovero    
    def get_diagnosi(self):
        return self.diagnosi
    def get_numero_giorni_degenza(self):
        return self.numero_giorni_degenza
    def get_numero_ricoveri(self):
        return self.numero_ricoveri
    
    
    #BLOCCO SET 
    def set_id_ricovero(self,id_ricovero):
        self.id_ricovero=id_ricovero
    def set_cod_fiscale(self,cod_fiscale):
        self.cod_fiscale=cod_fiscale
    def set_nome(self,nome):
        self.nome=nome 
    def set_cognome(self,cognome):
        self.cognome=cognome
    def set_regione_di_residenza(self,regione_di_residenza):
        self.regione_di_residenza=regione_di_residenza
    def set_data_inizio_ricovero(self,data_inizio_ricovero):
        self.data_inizio_ricovero=datetime.datetime.strptime(data_inizio_ricovero, "%d/%m/%Y")
    def set_data_fine_ricovero(self,data_fine_ricovero):
        self.data_fine_ricovero=datetime.datetime.strptime(data_fine_ricovero, "%d/%m/%Y")
    def set_patologie_cardiache(self,patologie_cardiache):
        self.patologie_cardiache=patologie_cardiache
    def set_patologie_respiratorie(self,patologie_respiratorie):
        self.patologie_respiratorie=patologie_respiratorie
    def set_esito_tampone_covid(self,esito_tampone_covid):
        self.esito_tampone_covid=esito_tampone_covid
    def set_tipologia_ricovero(self,tipologia_ricovero):
        self.tipologia_ricovero=tipologia_ricovero
    def set_diagnosi(self,diagnosi):
        self.diagnosi=diagnosi
    def set_numero_ricoveri(self,numero_giorni):
        self.numero_giorni=numero_giorni
        
        
        
    #PRIMO METODO, CALCOLA IL COSTO TOTALE DEL RICOVERO CHE L'AZIENDA OSPEDALIERA DEVE RICHIEDERE ALLA REGIONE DI COMPETENZA.
    #NELLO SPECIFICO PER TIPOLOGIA:
    #A)50 EURO GIORNALIERI TIPOLOGIA STANDARD 
    #B) 150 GIORNALIERI TIPOLOGIA SPECIALISTICO
    #NEL CASO IN CUI UN PAZIENTE E'POSITIVO AL COVID, AL TOTALE, CALCOLATO IN BASE ALLA TIPOLOGIA SI AGGIUNGE UNA QUOTA REGIONALE (q), CHE VARIA IN BASE ALLA DURATA DEL RICOVERO.
    def calcola_costo_Prestazione_Sanitaria(self):
            if 1>=self.numero_giorni_degenza<=3 and self.tipologia_ricovero == "STANDARD" and self.esito_tampone_covid=="NEGATIVO":
                self.costo_totale=50*self.numero_giorni_degenza
            elif self.numero_giorni_degenza >=4 and self.numero_giorni_degenza<=6 and self.tipologia_ricovero == "STANDARD" and self.esito_tampone_covid=="NEGATIVO":
                self.costo_totale=50*self.numero_giorni_degenza
            elif self.numero_giorni_degenza>6 and self.tipologia_ricovero == "STANDARD" and self.esito_tampone_covid=="NEGATIVO":
                self.costo_totale=50*self.numero_giorni_degenza
                
            elif 1>=self.numero_giorni_degenza<=3 and self.tipologia_ricovero == "SPECIALISTICO" and self.esito_tampone_covid=="NEGATIVO":
                self.costo_totale=150*self.numero_giorni_degenza
            elif 4>=self.numero_giorni_degenza<=6 and self.tipologia_ricovero == "SPECIALISTICO"and self.esito_tampone_covid=="NEGATIVO":
                self.costo_totale=150*self.numero_giorni_degenza
            elif self.numero_giorni_degenza>6 and self.tipologia_ricovero == "SPECIALISTICO" and self.esito_tampone_covid=="NEGATIVO":
                self.costo_totale=150*self.numero_giorni_degenza    
                
            elif 1>=self.numero_giorni_degenza<=3 and self.tipologia_ricovero == "STANDARD" and self.esito_tampone_covid== "POSITIVO":
                a=50*self.numero_giorni_degenza
                b=(a*2)/100
                self.costo_totale=a+b
            elif self.numero_giorni_degenza >=4 and self.numero_giorni_degenza<=6 and self.tipologia_ricovero == "STANDARD" and self.esito_tampone_covid== "POSITIVO":
                a=50*self.numero_giorni_degenza
                b=(a*4)/100
                self.costo_totale=a+b
            elif self.numero_giorni_degenza>6 and self.tipologia_ricovero == "STANDARD" and self.esito_tampone_covid== "POSITIVO":
                a=50*self.numero_giorni_degenza
                b=(a*6)/100
                self.costo_totale=a+b    
            elif 1>=self.numero_giorni_degenza<=3 and self.tipologia_ricovero == "SPECIALISTICO" and self.esito_tampone_covid== "POSITIVO":
                a=150*self.numero_giorni_degenza
                b=(a*0.3)/100
                self.costo_totale=a+b
            elif self.numero_giorni_degenza >=4 and self.numero_giorni_degenza<=6 and self.tipologia_ricovero == "SPECIALISTICO" and self.esito_tampone_covid== "POSITIVO":
                a=150*self.numero_giorni_degenza
                b=(a*0.5)/100
                self.costo_totale=a+b
            elif self.numero_giorni_degenza>6 and self.tipologia_ricovero == "SPECIALISTICO" and self.esito_tampone_covid== "POSITIVO":
                a=150*self.numero_giorni_degenza
                b=(a*1)/100
                self.costo_totale=a+b
            else:
                self.costo_totale="ERRORE"
            
            return self.costo_totale
    
        
        
    #IMPLEMENTO LA FUNZIONE CHE CALCOLA IL NUMERO DI GIORNI DI DEGENZA DI UN PAZIENTE, UTILIZZO LE FUNZIONALITA' DI DATETIME PER OTTENERE IL NUMERO DI GIORNI,
    #IN FORMATO ADEGUATO, CHE SIA CONFRONTABILE NEL CASO SIA DA INSERIRE IN METODI FUTURI.
    def numero_giorni_degenza(self):
        data_1=self.data_fine_ricovero
        data_2= self.data_inizio_ricovero
        #IL METODO AUTOMATICAMENTE NON PRENDE IN CONSIDERAZIONE L'ESTREMO SUPERIORE
        #SULLA BASE DELL'ESEMPIO CHE FIGURA NELLA TRACCIA D'ESAME LO PRENDO IN CONSIDERAZIONE AGGIUNGENDO +1
        self.numero_giorni_degenza= data_1.day - data_2.day+1    
        return self.numero_giorni_degenza         
        
    
    #IMPLEMENTO UN METODO CHE PERMETTE LA LETTURA DEL FILE TXT
    @classmethod
    def fromString(cls, string):
        parts = string.strip().split(":")
        id_ricovero=parts[0]
        cod_fiscale=parts[1]
        nome=parts[2]
        cognome=parts[3]
        regione_di_residenza=parts[4]
        data_inizio_ricovero=parts[5]
        data_fine_ricovero=parts[6]
        patologie_caridache=parts[7]
        patologie_respiratorie=parts[8]
        esito_tampone_covid=parts[9]
        tipologia_ricovero=parts[10]
        diagnosi=parts[11]
        return cls(id_ricovero,cod_fiscale,nome,cognome,regione_di_residenza,data_inizio_ricovero,data_fine_ricovero,patologie_caridache,patologie_respiratorie,esito_tampone_covid,tipologia_ricovero,diagnosi)
      
        
    
    def __lt__(self, other):
        if self.tipologia_ricovero<other.tipologia_ricovero:
            return True 
        elif self.numero_giorni_degenza < other.numero_giorni_degenza:
            return True
        else:
            return False
        
    
    



    
    
    

