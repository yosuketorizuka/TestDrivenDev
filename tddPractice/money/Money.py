class Money:
    def __init__(self, arg):
        self.amount = arg
    
    def equals(self, object):
        money = object
        # 2つのMoneyオブジェクトの金額と実クラスが正しいときのみ、Trueを返す
        #print(type(self))
        #print(type(money))
        return (self.amount == object.amount) and (type(self) == type(money))
        #return self.amount == money.amount