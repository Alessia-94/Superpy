#Model: Profit, this is the class profit and is where I define its structure

class Profit:
    def __init__(self, id, type, profit):
        self.id = id
        self.type = type
        self.profit = float(profit) 

# Method to facilitate the saving operation in the data base
    def get_profit_as_row(self):
        return[self.id, self.type, self.profit]
        