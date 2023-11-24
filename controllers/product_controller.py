#metodo caricamento profitto
#metodo lista dei prodotti in base a expired etc.
#dobbiamo fare i metodi per gestire tutti i dati

from repository.product_repository import Product_repository
from .profit_controller import Profit_controller # importiamo il controller e non il repositori, perche solo i controller si parlano. storia delle responsability. Per esempio check profit, si fa nell'handler
from .date_controller import Date_controller
from repository.product_repository import Product

class Product_controller:
    profit_controller = Profit_controller() #inizializziamo il controller dei profitti, costruttore trattato come un metodo
    date_controller = Date_controller()
    product_repository = Product_repository()
    products = list () 

    def __init__(self):
        self.products = self.product_repository.product_list #stiamo assegnado al controller la lista dei prodotti, stiamo riempendo list products
        self.enrich_products()

    def enrich_products(self): #nell'init facciamo un giro di tutti i prodotti e assegnare le nuove info, per far calcolare a ogni prodotto le info giuste 
        for product in self.products:
            product: Product
            profit = self.profit_controller.get_profit_by_type(product.product_type) 
            product.set_profit(profit)
            product.compute_selling_price()
            product.compute_expiration(self.date_controller.get_current_date())
            product.compute_on_sale(self.date_controller.get_current_date())

    def test_product(self):
        for p in self.products:
            p: Product
            print (str(p.product_name) + " " + str(p.product_selling_price) + " " + str(p.product_expired))

        
        