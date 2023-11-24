# this is the class product entity del prodotto
from .profit import Profit
from .superpy_time import SuperpyTime

class Product:

    def __init__(self, product_id, product_type, product_name, product_buy_date, product_buy_price, product_selling_price, product_sell_date, product_expiration_date, product_expired, product_sold, product_onsale):
        self.profit: Profit = None   # questa e la classe importata dall'altro casse, proprieta classe profit. Stiamo inizializzando la proprieta profitto con la classe profit, lui prende solo lo schema della classe, e vuoto dentro. Poi dopo gli diciamo quali valori prendere. Questo lo facciamo nell'handler
        self.product_id = product_id
        self.product_type = product_type
        self.product_name = product_name
        self.product_buy_date = SuperpyTime(product_buy_date) #lo istanziamo cin superbytime e lo trasforma in data. Vogliamo utilizzare tutti i metodi della classe tempo. 
        self.product_buy_price = product_buy_price
        self.product_selling_price = product_selling_price
        self.product_sell_date = SuperpyTime(product_sell_date)
        self.product_expiration_date = SuperpyTime(product_expiration_date) #lo istanziamo cin superbytime 
        self.product_expired = product_expired
        self.product_sold = product_sold
        self.product_onsale = product_onsale
# qui quello che devo calcolare 
    def set_profit(self, profit):
        self.profit = profit 

    def compute_selling_price(self):
        self.selling_price = self.product_buy_price * self.profit.profit #1.2 etc
        if self.product_onsale:
            self.selling_price * 0.5 # si sconta al 50 percento se il prodotto e in salto


    def compute_expiration(self, current_time): 
        if self.product_expiration_date.current_date_gt(current_time): #current date gr e il metodo di superpy, lo abbiamo istanziato come superpy quindi possiamo usarlo
            self.product_expired = True
        else:
            self.product_expired = False

            
             #se la data di expiration e maggiore della data che mi stai passando 
    '''ciao
    sssss'''
    def compute_on_sale(self, current_time):
        self.product_onsale = False #lo impostiamo in false, se passa i controlli va nel secondo if, se non e scaduto e mancano 3 giorni alla scanza diventa true
        if self.product_expiration_date.current_date_lt(current_time):
            if self.product_expiration_date.time_delta(current_time) <= 3: #3 gg scadenza
                self.product_onsale = True
