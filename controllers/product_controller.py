#Product controller, here we have to make all the methods to handle all the data of the products to make all the lists that I need (prodcut, expired etc). To do so I need to import product repository, profit controller, data controller. We import the profit and data controller because they have already all the info "checked" with which the product controller needs to work with

from repository.product_repository import Product_repository
from models.superpy_time import SuperpyTime
from .profit_controller import Profit_controller 
from .date_controller import Date_controller
from repository.product_repository import Product
import datetime

#I make the class of the product controller and I initialise the profit controller, date controller, product repository as methods, and an empty list for the products. In this way I can use their methods
class Product_controller:
    profit_controller = Profit_controller() 
    date_controller = Date_controller()
    product_repository = Product_repository()
    products = list () 

#here I "fill" the list of the product with the data from the product repository 
    def __init__(self):
        self.products = self.product_repository.product_list 
        self.enrich_products()
        self.save_all_products()

#here I "loop" the product list to assign these new information in order to compute the correct information.
    def enrich_products(self):
        for product in self.products:
            product: Product
            profit = self.profit_controller.get_profit_by_type(product.product_type) 
            product.set_profit(profit)
            product.compute_selling_price()
            product.compute_expiration(self.date_controller.get_current_date())
            product.compute_on_sale(self.date_controller.get_current_date())

    def save_all_products(self):
        self.product_repository.save_products(self.products)
        
    def get_product_list(self):
        return self.products
    
  # updated to date product list      
    def get_real_time_product_list(self):
        results = list()
        for p in self.products:
            p: Product
            if self.date_controller.get_current_date().current_date_gte(p.product_buy_date):
                results.append(p)
        return results

# I loop the list of the product. If product type is equal to type, add it to the list
    def get_product_list_by_type(self, type):
        results = list()
        for p in self.get_real_time_product_list():
            p: Product
            if p.product_type == type:
                results.append(p)
        return results

#List of all the products not sold. If a product has not been sold and is not expired, add it to the list     
    def get_available_product_list_with_expiring_date(self):
        results = list()
        for p in self.get_real_time_product_list():
            p: Product
            if not p.product_sold and not p.product_expired:
                results.append(p)
        return results

 
    def get_available_product_list(self):
        results = list()
        for p in self.get_real_time_product_list():
            p: Product
            if not p.product_sold and not p.product_expired:
                results.append(p)
        return results

# list of all the product not sold.     
    def get_all_available_or_expired(self):
        results = list()
        for p in self.get_real_time_product_list():
            p: Product
            if not p.product_sold:
                results.append(p)
        return results

# list of all the product expired            
    def get_all_expired_products(self):
        results = list()
        for p in self.get_real_time_product_list():
            p: Product
            if(p.product_expired):
                results.append(p)
        return results

# list of all the product by name (amount) (not case sensitive)      
    def get_all_products_by_name(self, product_name):
        results = list()
        for p in self.get_real_time_product_list():
            p:Product
            if(str.upper(p.product_name) == str.upper(product_name)):
                results.append(p)
        return results

# method to interact with the product list. In this case I can indicate a product that can be sold, and if it is  not present in the available list get as result NOT FOUND or OUT OF ORDER     
    def sell_product_by_name(self, product_name):
        products = self.get_all_available_products_by_name(product_name)
        if(len(products) < 1):
            return "[red]" + product_name + " NOT FOUND[/red]"
        for p in products:
            p: Product
            if(not p.product_sold):
                p.sell_product(self.date_controller.get_current_date())
                return "[green]" + p.product_name + " sold in date: " + str(p.product_sell_date) + "[/green] [blue]at this price: " + str(p.product_selling_price) + "[/blue]" 
        return "[red]" + product_name + " OUT OF ORDER[/red]"

# list of all the product available (not case sensitive)   
    def get_all_available_products_by_name(self, product_name):
        results = list()
        for p in self.get_real_time_product_list():
            p: Product
            if((str.upper(p.product_name) == str.upper(product_name)) and (not p.product_expired)):
                results.append(p)
        return results

# list of all the product sold  
    def get_all_sold_products(self):
        results = list()
        for p in self.get_real_time_product_list():
            p: Product
            if(p.product_sold):
                results.append(p)
        return results

# list of all the product on sale --> needs to be checked
    def get_all_on_sale_products(self):
        results = list()
        for p in self.get_real_time_product_list():
            p: Product
            if(p.product_onsale and not p.product_expired):
                results.append(p)
        return results

# list of all sold products in a specific time range   
    def get_all_sold_products_in_time_range(self, t1, t2):
        results = list()
        if(type(t1) == str): t1 = SuperpyTime(t1)
        if(type(t2) == str): t2 = SuperpyTime(t2)
        if(type(t1) == datetime.datetime): t1 = SuperpyTime(datetime.datetime.strftime(t1, "%Y-%m-%d"))
        if(type(t2) == datetime.datetime): t2 = SuperpyTime(datetime.datetime.strftime(t2, "%Y-%m-%d"))
        sold_products = self.get_all_sold_products()
        for p in sold_products:
            p: Product
            if(p.product_sell_date.current_date_gte(t1) and p.product_sell_date.current_date_lte(t2)):
                results.append(p)
        return results

# list of all bought products in a specific time range       
    def get_all_bought_products_in_time_range(self, t1, t2):
        results = list()
        if(type(t1) == str): t1 = SuperpyTime(t1)
        if(type(t2) == str): t2 = SuperpyTime(t2)
        if(type(t1) == datetime.datetime): t1 = SuperpyTime(datetime.datetime.strftime(t1, "%Y-%m-%d"))
        if(type(t2) == datetime.datetime): t2 = SuperpyTime(datetime.datetime.strftime(t2, "%Y-%m-%d"))
        bought_products = self.products
        for p in bought_products:
            p: Product
            if(p.product_buy_date.current_date_gte(t1) and p.product_buy_date.current_date_lte(t2)):
                results.append(p)
        return results

 # Method to calculate the profit of the supermaker in a specific time range          
    def calculate_profit_in_time_range(self, t1: str, t2: str):
        result = 0
        t1 = SuperpyTime(t1)
        t2 = SuperpyTime(t2)
        sold_products = self.get_all_sold_products()
        for p in sold_products:
            p: Product
            if(p.product_sell_date.current_date_gte(t1) and p.product_sell_date.current_date_lte(t2)):
                result += p.get_net()
        return result

 # Method to calculate the revenue of the supermaker in a specific time range    
    def calculate_revenue_in_time_range(self, t1: str, t2: str):
        result = 0
        t1 = SuperpyTime(t1)
        t2 = SuperpyTime(t2)
        sold_products = self.get_all_sold_products()
        for p in sold_products:
            p: Product
            if(p.product_sell_date.current_date_gte(t1) and p.product_sell_date.current_date_lte(t2)):
                result += p.product_selling_price
        return result

 # Methods to create a new csv files where to export the updated list of the sold products/all products/expired products/available products 
    def export_sold_products(self):
        fn = "sold_products_export.csv"
        all_sold = self.get_all_sold_products()
        self.product_repository.export_products(all_sold, fn)
        return fn
    
    def export_all_products(self):
        fn = "all_products_export.csv"
        self.product_repository.export_products(self.products, fn)
        return fn
    
    def export_expired_products(self):
        fn = "expired_products_export.csv"
        all_expired = self.get_all_expired_products()
        self.product_repository.export_products(all_expired, fn)
        return fn

    def export_available_products(self):
        fn = "available_products_export.csv"
        all_available = self.get_available_product_list_with_expiring_date()
        self.product_repository.export_products(all_available, fn)
        return fn
    
# method to interact with the product list. In this case I can add a new product to the list of the supermarket, and I build its structure to insert its characteristics (ID, Name, Type, buy date etc..)  
    def buy_new_product(self, params):
        new_id = self.product_repository.get_max_id()
        buy_date = datetime.datetime.strftime(self.date_controller.get_current_date().current_date, "%Y-%m-%d")
        p = Product(new_id, params[1], params[0], buy_date, params[2], 0, None, params[3], 0, 0, 0)
        self.products.append(p)
        self.enrich_products()
        self.save_all_products()
        return p
    
    def test_product(self):
        for p in self.products:
            p: Product
            print (str(p.product_name) + " " + str(p.product_selling_price) + " " + str(p.product_expired))

