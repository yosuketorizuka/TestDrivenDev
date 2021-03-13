class Dollar:

    def __init__(self, arg):
        self.amount = arg
    
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def equals(self, object):
        Dollar.dollar = object
        return self.amount == object.amount