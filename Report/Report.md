# Report
## Selected topic

- Staticmethod
- Profit Repository
- Profit controller 

## Static method

I decided to use a “staticmethod” in order to load the data from the csv files (one for the time, one for the profit and one for the product). In object oriented, methods usually work according instantiation. For example. When I instantiate the product class, this class have different instances (apple, oranges etc). The methods of the class will operate on the information of that specific object (apple price is different from the one of an orange). The static method behaves the opposite, it returns always the same information independently from the instances. I chose to use this because in this specific case, the data_base has to only load the data. Independently from the instances. Each repository (profit, product, time) will “re-call” the data_base to import its own data.

```sh
import csv
from models.product import Product
from models.profit import Profit


class Data_Base:
    time_table = "dbo/date.csv"
    profit_table = "dbo/profit.csv"
    product_table = "dbo/product.csv" 
    product_table_header = None 
    time_table_header = None
    profit_table_header = None 

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

```

## Profit repository

The repository has the role to handle specific data (for example reading -writing – rewriting info from the database). In the case of the profit repository, I decided to organise its information using a dictionary, because it is an easy way through the use of keys (type) to refer to specific values (for example profit). The data have been loaded from the Data_base and the “empty structure” of the dictionary have been imported from the Profit model. The dictionary “profit_table” has been “filled” using the for loop. By doing so I have loaded all the profits from the database. Now in the repository I  have “built” a dictionary using that data. This dictionary will be accessible to the controllers to handles these data.
```sh
from dbo.data_base import Data_Base
from models.profit import Profit 

class Profit_repository:

    profit_table = dict()

    def __init__(self):
        self.load_profit()

    def load_profit(self):
        profits = Data_Base.loadprofitDB() # here we indicate the pointer to the file
        self.profit_table.clear()
        for line in profits:
            self.profit_table [line[1]] = Profit(line[0], line[1], line[2]) 
```

## Check Profit controller

I put a research method in the dictionary called “get_profit_by_type”. I do this to check that the information about the types of the products are there. Types are important information because they are the keys of my dictionary. If the type is not in the dictionary, return None. This is a test to check that for each type I have a profit. If for example I ask for a type that is not included in the profit.csv, I get None. This is useful to avoid errors. In case I ask for a type that is not present, my program will not crush but print None.

```sh
class Profit_controller:
    profits = dict ()
    profit_repository = Profit_repository() 
  
    def __init__(self):
        self.profits = self.profit_repository.profit_table
        
    def get_profit_by_type (self, type):
        if type in self.profits.keys():
            return self.profits.get(type) 
        else:
            return None 
  ```    

