#Data_base: this is the class data_base.
import csv
from models.product import Product
from models.profit import Profit

#here I make a class data base where I indicate where the file.csv are saved. I indicate also the "header" which are the first line of the csv. They do not have a value, but I will assign it when I read the file
class Data_Base:
    time_table = "dbo/date.csv"
    profit_table = "dbo/profit.csv"
    product_table = "dbo/product.csv" 
    product_table_header = None 
    time_table_header = None
    profit_table_header = None 

#static classes. The data_base is only one and it load the datas, indipendendly from which sort of data. We do tese operation for example for loading data, re-writing data and export data

    @staticmethod
    def loadtimeDB():
        f = open(Data_Base.time_table, "r") # we indicate where is the file, and that we need to only read the data
        csv_file = csv.reader(f, delimiter=",") # we use the method csv to read the data as a string and delimite the data with a comma
        Data_Base.time_table_header = next(csv_file) # we skip the first line of the csv file (headers)
        return csv_file 
    
    @staticmethod   
    def loadprofitDB():
        f = open(Data_Base.profit_table, "r")
        csv_file = csv.reader(f, delimiter=",")
        Data_Base.profit_table_header = next(csv_file) 
        return csv_file
    
    @staticmethod   
    def loadproductDB():
        f = open(Data_Base.product_table, "r")
        csv_file = csv.reader(f, delimiter=',')
        Data_Base.product_table_header = next(csv_file)
        return csv_file

# here I use the static method to "re-write" the new date calculated in the date_controller in case we retrieve/advance in time
    @staticmethod
    def savetimeDB(value):
        f = open(Data_Base.time_table, "w+", newline="")
        csv_file = csv.writer(f, delimiter=",")
        row_value = [value]
        csv_file.writerow(Data_Base.time_table_header)
        csv_file.writerow(row_value)


# here I use the static method to"re-write" the new products list updated 
    def saveproductDB(products):
        f = open(Data_Base.product_table, "w+", newline="")
        csv_file = csv.writer(f, delimiter=",")
        csv_file.writerow(Data_Base.product_table_header)
        for p in products:
            p: Product
            row_value = p.get_product_as_row()
            csv_file.writerow(row_value)

# here I use the static method to export the new data of the products updated
    @staticmethod
    def exprotProducts(products, file_name):
        file_name = "export/" + file_name
        f = open(file_name, "w+", newline="")
        csv_file = csv.writer(f, delimiter=",")
        csv_file.writerow(Data_Base.product_table_header)
        for p in products:
            p: Product
            row_value = p.get_product_as_row()
            csv_file.writerow(row_value)

# here I use the static method to re-write the new profits updated
    @staticmethod
    def saveprofitDB (profits):
        f = open(Data_Base.profit_table, "w+", newline="")
        csv_file = csv.writer(f, delimiter=",")
        csv_file.writerow(Data_Base.profit_table_header)
        for p in profits:
            p: Profit
            row_value = p.get_profit_as_row()
            csv_file.writerow(row_value)