import Money

class Franc(Money.Money):
    
    def times(self, multiplier):
        return Franc(self.amount * multiplier)