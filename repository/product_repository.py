#Repository: product repository, i load here my database and with the data imported I build a list

from dbo.data_base import Data_Base
from models.product import Product 

#I build the list of the products, by loading the products data from the database. In the method I indicate how I want my list to be build
class Product_repository:
    product_list = list()

    def __init__(self):
        products = Data_Base.loadproductDB() 
        for product in products:
            self.product_list.append (Product(product[0], product[1], product[2], product[3], product[4], product[5], product[6], product[7], product[8], product[9], product[10]))

# Here I indicate which command the database has to do: save an updated version of my product list, exports my product list
    def save_products(self, products):
        Data_Base.saveproductDB(products)

    def export_products(self, products, file_name):
        Data_Base.exprotProducts(products, file_name)

# Here I used this method to add new "ID" in case I add a new product to the list
    def get_max_id(self):
        return len(self.product_list)
