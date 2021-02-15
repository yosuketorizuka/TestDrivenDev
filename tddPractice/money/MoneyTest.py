import unittest

# テストをしたいモジュールをimportする
import dollar

# クラス名はなんでもよいが、unittest.TestCaseの継承は必要
class MoneyTest(unittest.TestCase):

    def testMutiplication(self):
           
        five = dollar.Dollar(5)
        
        product = five.times(2)
        self.assertEqual(10, product.amount)

        product = five.times(3)
        self.assertEqual(15, product.amount)

if __name__ == '__main__':
    unittest.main()