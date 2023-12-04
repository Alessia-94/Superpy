# Imports
import argparse
import csv
import datetime as dt
from controllers.product_controller import Product_controller
from controllers.date_controller import Date_controller
from models.product import Product 
import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
pr = Product_controller()
dr = Date_controller()
console = Console()


'''Argparse is a method that help the user to interface the program 
in an easy way. Through the use of comand, we can do some operations and get results. 
Using the "If" construction I can associate a command to an operation

CONSTRUCTION: 
- we define the command using parse.add_argument --> parser.add_argument(abbreviation argument "-l", complete argument "--list", explanation, action="store_time")
- in the def, i print what I want the command to show to the user
- using the if (if args.) structure I associate the command to the corresponding compute'''

def main():
    parser = argparse.ArgumentParser(prog="Superpy", description="Superpy Program", epilog="Thanks for using Superpy")
    parser.add_argument('-l', '--list', help='Print all products', action='store_true')
    #to check!!
    parser.add_argument('-la', '--list_available', help='Print all products available with expiring date', action='store_true')
    parser.add_argument('-e', '--expired', help='Print all expired products', action='store_true')
    # what is printing
    parser.add_argument('-ad', '--advance_days', help='Advance date for n days')
    parser.add_argument('-rd', '--retreat_days', help='Retreat date for n days')
    parser.add_argument('-rt', '--reset_time', help='Reset time to today', action='store_true')
    parser.add_argument('-sp', '--sell_product', help='Sell a product')
    parser.add_argument('-ls', '--list_sold', help='Print all sold products', action='store_true')
    parser.add_argument('-pr', '--profit_revenue', help='Print all profits and revenue of sold products in a specified time ex. 2023-10-01/2023-11-01')
    parser.add_argument('-ex', '--export', help='Export in csv format sold products (s), all products (p), expired products (e), available products (a)')
    parser.add_argument('-p', '--plot', help='Plot products sold by date range ex. 2023-10-01/2023-11-01')
    parser.add_argument('-bp', '--buy_product', nargs='+', help='Buy a product Name Type Price Expiration(2023-12-01)')
    #c check! not working
    parser.add_argument('-pt', '--product_table', help='Print product table', action='store_true')
    #check -hulp text
    args = parser.parse_args()
    
    if args.list: 
        all_products()
    elif args.list_available: 
        get_available_product_list_with_expiring_date()
    elif args.expired: 
        all_expired_products()
    elif args.advance_days: 
        dr.advance_days(int(args.advance_days)) #check se ci sta e se ce esegui
        all_expired_products()
    elif args.retreat_days: 
        dr.retreat_days(int(args.retreat_days)) #check se ci sta e se ce esegui
        all_expired_products()
    elif args.reset_time:
        dr.reset_time_to_today()
    elif args.sell_product:
        pr.sell_product_by_name(args.sell_product)
        pr.save_all_products()
        all_sold_products()
    elif args.list_sold:
        all_sold_products()
    elif args.buy_product:
        print_products(pr.buy_new_product(args.buy_product))
    elif args.profit_revenue:
        dates: str = args.profit_revenue
        date1 = dates.split("/")[0]
        date2 = dates.split("/")[1]
        all_sold_products_in_time_range(date1, date2)
        profit_in_time_range(date1,date2)
        revenue_in_time_range (date1, date2)
    elif args.export:
        export_command = args.export
        if export_command == "s" or export_command == "S":
            console.print("[cyan]Export done in file:[/cyan] [green]" + pr.export_sold_products() + "[/green]")
        elif export_command == "p" or export_command == "P":
            console.print("[cyan]Export done in file:[/cyan] [green]" + pr.export_all_products() + "[/green]")
        elif export_command == "e" or export_command == "E":
            console.print("[cyan]Export done in file:[/cyan] [green]" + pr.export_expired_products() + "[/green]")
        elif export_command == "a" or export_command == "A":
            console.print("[cyan]Export done in file:[/cyan] [green]" + pr.export_available_products() + "[/green]")
    elif args.plot:
        dates: str = args.plot
        date1 = dates.split("/")[0]
        date2 = dates.split("/")[1]
        plot_data(date1, date2)
    elif args.product_table:
        print_products(pr.get_product_list)
        
def print_products(products):
    table = Table(title="Overview product at date" + render_date(dr.get_current_date().current_date))
    table.add_column("Product", justify="right", style="cyan", no_wrap=True)
    table.add_column("Type", style="green")   
    table.add_column("Buy_date", style="green")
    table.add_column("Selling_date", style="green")
    table.add_column("Bought_price", style="green")
    table.add_column("Sold", style="green")
    table.add_column("Selling_price", style="green")
    table.add_column("Expired", style="green")
    table.add_column("Expired date", style="green")
    if(not type(products) == list): products = [products]
    for p in products:
        p: Product
        table.add_row(p.product_name, p.product_type, render_date(p.product_buy_date.current_date), render_date(p.product_sell_date.current_date), str(p.product_buy_price), render_bool(p.product_sold), str(round(p.product_selling_price, 2)), render_bool(p.product_expired), render_date(p.product_expiration_date.current_date))
    console.print(table)

def render_bool(b):
    if(b): return "YES"
    return "NO"

def render_date(date):
    if(date == None): return ""
    return str(date)

def get_available_product_list_with_expiring_date():
    all_products = pr.get_available_product_list_with_expiring_date()
    print_products(all_products)

def all_products():
    all_products = pr.get_product_list()
    print_products(all_products)

def all_expired_products():
    all_products = pr.get_all_expired_products()
    print_products(all_products)

def all_sold_products():
    all_sold_products = pr.get_all_sold_products()
    print_products(all_sold_products)

def all_sold_products_in_time_range(date1, date2):
    products = pr.get_all_sold_products_in_time_range(date1, date2)
    print_products(products)

def profit_in_time_range(date1, date2):
    profit = pr.calculate_profit_in_time_range(date1,date2)
    console.print("Profit between" + date1 + "and" + date2 + " " + str(round(profit, 2)), style="bold red")

def revenue_in_time_range(date1, date2):
    revenue = pr.calculate_revenue_in_time_range(date1,date2)
    console.print("Revenue between" + date1 + "and" + date2 + " " + str(round(revenue, 2)), style="bold green")

def plot_data(date1, date2):
    dates = dr.get_time_array_in_time_range(date1, date2)
    products_s = list()
    dates_s = list()
    for d in dates:
        d: dt.datetime
        products_s.append(len(pr.get_all_sold_products_in_time_range(d, d))) #check
        dates_s.append(str(d.day) + "/" + str(d.month))
    plt.style.use("ggplot")
    plt.title("Sold products by date in time range" + dates_s[0] + " - " + dates_s[len(dates_s)-1])
    plt.bar(dates_s, products_s, width=0.5)
    plt.show()


if __name__ == "__main__":
    main()
