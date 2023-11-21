# this is the class product entity del prodotto
from profit import Profit

class Product:

    def __init__(self, product_id, product_type, product_buy_date, product_buy_price, product_selling_price, product_sell_date, product_expiration_date, product_expired, product_onsale):
        self.profit = Profit()    # questa e la classe importata dall'altro casse, proprieta classe profit. Stiamo inizializzando la proprieta profitto con la classe profit, lui prende solo lo schema della classe, e vuoto dentro. Poi dopo gli diciamo quali valori prendere. Questo lo facciamo nell'handler
        self.product_id = product_id
        self.product_type = product_type
        self.product_buy_date = product_buy_date
        self.product_buy_price = product_buy_price
        self.product_selling_price = product_selling_price
        self.product_sell_date = product_sell_date
        self.product_expiration_date = product_expiration_date
        self.product_expired = product_expired
        self.product_onsale = product_onsale
# qui quello che devo calcolare 
    def set_profit(self, profit):
        self.profit = profit 

    def compute_selling_price(self):
        self.selling_price = self.product_buy_price + (self.product_buy_price * self.profit.profit / 100)


    def compute_expiration(self):
        pass

    def compute_on_sale(self):
        pass
