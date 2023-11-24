#Model: product this is the class product. Here I define all its known characteristics and as well define the characteristics that needs to be compute.

from .profit import Profit
from .superpy_time import SuperpyTime

'''In the product class I imported also the profit class, and I defined as characteristic of the product
sel.profit: Profit = None --> this initialised the Profit from the profit class (model --> profit). 
We take only the scheme of the class, the class itself is empty. We will fill it in the controller

self.product_buy_date and self.product_expiration_date = we instantiate it with SuperpyTime that trasform the string into data, in this way we can
use all the method of the SuperpyTime class'''

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
        self.product_expired = product_expired
        self.product_sold = product_sold
        self.product_onsale = product_onsale

# here I write all the data that are not available and that I need to calculate

    def set_profit(self, profit):
        self.profit = profit 

#if the product is close to the expired date, its selling price will be discounted of 50%

    def compute_selling_price(self):
        self.selling_price = self.product_buy_price * self.profit.profit 
        if self.product_onsale:
            self.selling_price * 0.5 

#We have istantiate the Superpytime, so we can use its methods = current_date_gt
#if the expirede date is greater than the date you are passing me......

    def compute_expiration(self, current_time): 
        if self.product_expiration_date.current_date_gt(current_time):
            self.product_expired = True
        else:
            self.product_expired = False

#we assign to the field " self.product_onsale" False. If it pass all the "checks" of the second if: if it is not expired AND are missing 3 days to the expired date, it becomes true

    def compute_on_sale(self, current_time):
        self.product_onsale = False 
        if self.product_expiration_date.current_date_lt(current_time):
            if self.product_expiration_date.time_delta(current_time) <= 3: #3 gg scadenza
                self.product_onsale = True
