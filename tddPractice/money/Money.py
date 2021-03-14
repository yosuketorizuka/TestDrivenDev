class Money:
    def __init__(self, arg):
        self.amount = arg
    
    def equals(self, object):
        Money.money = object
        return self.amount == object.amount