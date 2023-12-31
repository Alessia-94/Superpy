#Model: product this is the class product. Here I define all its known characteristics and as well define the characteristics that needs to be compute.

from .profit import Profit
from .superpy_time import SuperpyTime
import datetime as dt

'''In the product class I imported also the profit class, and I defined as characteristic of the product
self.profit: Profit = None --> this initialised the Profit from the profit class (model --> profit). 
I take only the scheme of the class, the class itself is empty. i will fill it in the controller

Superpy class: product_buy_date, product_sell_date and product_expiration_date = I instantiate them with SuperpyTime that trasform the string into data, in this way I can
use all the methods of the SuperpyTime class'''

class Product:

    def __init__(self, product_id, product_type, product_name, product_buy_date, product_buy_price, product_selling_price, product_sell_date, product_expiration_date, product_expired, product_sold, product_onsale):
        self.profit: Profit = None   
        self.product_id = product_id
        self.product_type = product_type
        self.product_name = product_name
        self.product_buy_date = SuperpyTime(product_buy_date) 
        self.product_buy_price = float(product_buy_price)
        self.product_selling_price = product_selling_price
        self.product_sell_date = SuperpyTime(product_sell_date)
        self.product_expiration_date = SuperpyTime(product_expiration_date) 
        self.product_expired = bool(int(product_expired)) # product expired will be an integer 0 or 1, transformed into boolean become False-true
        self.product_sold = bool(int(product_sold))
        self.product_onsale = bool(int(product_onsale))

# here I write all the data that are not available and that I need to calculate

    def set_profit(self, profit):
        self.profit = profit 

#if the product is close to the expired date, its selling price will be discounted of 50%

    def compute_selling_price(self):
        self.product_selling_price = self.product_buy_price * self.profit.profit 
        if self.product_onsale:
            self.product_selling_price * 0.5 

#To compute the expiration date I need to import Superpytime because it has the date not as text but already converted in date. By importing it I can also use its method (for example "current_date_lt")
    def compute_expiration(self, current_time): 
        if self.product_expiration_date.current_date_lt(current_time):
            self.product_expired = True
        else:
            self.product_expired = False

#To compute the on_sale, I assign to the field " self.product_onsale" False. If it pass all the "checks" of the second if: if it is not expired AND are missing 3 days to the expired date, it becomes true
    def compute_on_sale(self, current_time):
        self.product_onsale = False 
        if self.product_expiration_date.current_date_lt(current_time):
            if self.product_expiration_date.time_delta(current_time) <= 3: #3 gg scadenza
                self.product_onsale = True

#Here I continue to compute data (indicated as name of the methods) that are not directly given by the database of the products)
    def get_product_buy_date_as_string(self):
        if(self.product_buy_date is None or self.product_buy_date.current_date is None): return ""
        return dt.datetime.strftime(self.product_buy_date.current_date, "%Y-%m-%d")

    def get_product_sell_date_as_string(self):
        if(self.product_sell_date is None or self.product_sell_date.current_date is None): return ""
        return dt.datetime.strftime(self.product_sell_date.current_date, "%Y-%m-%d")
    
    def get_product_expiration_date_as_string(self):
        if(self.product_expiration_date is None or self.product_expiration_date.current_date is None): return ""
        return dt.datetime.strftime(self.product_expiration_date.current_date, "%Y-%m-%d")
    
    def get_product_expired_as_number_string(self):
        if(self.product_expired): return "1"
        return "0"
    
    def get_product_sold_as_number_string(self):
        if(self.product_sold): return "1"
        return "0"
    
    def get_product_onsale_as_number_string(self):
        if(self.product_onsale): return "1"
        return "0"
    
    def get_product_as_row(self):
        return [self.product_id, self.product_type, self.product_name, self.get_product_buy_date_as_string(), str(self.product_buy_price), str(self.product_selling_price), self.get_product_sell_date_as_string(), self.get_product_expiration_date_as_string(), self.get_product_expired_as_number_string(), self.get_product_sold_as_number_string(), self.get_product_onsale_as_number_string()]
    
    def sell_product(self, sell_date):
        self.product_sold = True
        self.product_sell_date = sell_date

    def get_net(self):
        return self.product_selling_price - self.product_buy_price
    

    