# Imports
import argparse
import csv
from datetime import date
from controllers.product_controller import Product_controller



# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

def main():
    pr = Product_controller() #abbiamo innescato il costruttore, nel costruttore carichiamo il repository
    pr.test_product()

if __name__ == "__main__":
    main()



