#Data_base: this is the class data_base.

import csv

class Data_Base:
    time_table = "date.csv"
    profit_table = "profit.csv"
    product_table = "product.csv"

#static class, The data_base is only one and it load the datas, indipendendly from which sort of data.

    @staticmethod
    def loadtimeDB():
        f = open(Data_Base.time_table, "r") # we indicate where is the file, and that we need to only read the data
        csv_file = csv.reader(f, delimiter=",") # we use the method csv to read the data as a string and delimite the data with a comma
        next(csv_file) # we skip the first line of the csv file (headers)
        return csv_file 
    
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

