#Model: Profit, this is the class profit

class Profit:
    def __init__(self, id, type, profit):
        self.id = id
        self.type = type
        self.profit = float(profit) 

    def get_profit_as_row(self):
        return[self.id, self.type, self.profit]
        