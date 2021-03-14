import Money

class Dollar(Money.Money):

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)