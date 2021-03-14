class Franc:

    def __init__(self,arg):
        self.amount = arg

    def times(self, multiplier):
        return Franc(self.amount * multiplier)

    def equals(self, object):
        Franc.Franc = object
        return self.amount == object.amount