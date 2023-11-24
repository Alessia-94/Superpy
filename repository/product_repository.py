#Repository: product repository, i load here my database and with the data imported I build a list

from dbo.data_base import Data_Base
from models.product import Product #importiamo la classe

class Product_repository:
    product_list = list()

    def __init__(self):
        products = Data_Base.loadproductDB() 
        for product in products:
            self.product_list.append (Product(product[0], product[1], product[2], product[3], product[4], product[5], product[6], product[7], product[8], product[9], product[10]))
