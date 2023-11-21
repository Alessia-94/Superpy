# Imports
import argparse
import csv
from datetime import date
from repository import profit_repository

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

def main():
    pr = profit_repository.Profit_repository() #abbiamo innescato il costruttore, nel costruttore carichiamo il repository
    print(pr.profit_table)


