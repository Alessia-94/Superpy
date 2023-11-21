import csv

class Data_Base:
    time_table = "date.csv"
    profit_table = "profit.csv"
    product_table = "product.csv"

    @staticmethod
    def loadtimeDB():
        f = open(Data_Base.time_table, "r")
        csv_file = csv.reader(f, delimiter=",") #f csv e il modulo che stiamo importando, reader e un metodo del modulo, restituisce un lettore del file, restituisce il puntatore del file. formatta e prende i valori separatamente per , f e il file proprio 
        next(csv_file) 
        return csv_file #il puntatore ppunta alla riga successiva no header
    
    @staticmethod   
    def loadprofitDB():
        f = open(Data_Base.profit_table, "r")
        csv_file = csv.reader(f, delimiter=",")
        next(csv_file) 
        return csv_file
    
    @staticmethod   
    def loadproductDB():
        f = open(Data_Base.product_table, "r")
        csv_file = csv.reader(f, delimiter=",")
        next(csv_file) 
        return csv_file


        #METODO statico, l-annotation il metodo deve comportarsi in modo. istanziamo il prodoctto come latte, metodo prezzo. metodo statico, va al di la dell'istanzazione, da sempre la stessa informazione. istanza della classe statica e uguale per tutti.
        # data base, solo uno carica i dati, indipendemente dai dati. ogni repositori chiamera il database. tutti quanti vedono gli stessi dati.
        # f riferisce lapertura del file a una variabile. ci riferiamo alla classe, e prendiamo il valore statico