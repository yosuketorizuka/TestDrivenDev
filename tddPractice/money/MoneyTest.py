import unittest

# テストをしたいモジュールをimportする
import Dollar

# クラス名はなんでもよいが、unittest.TestCaseの継承は必要
class MoneyTest(unittest.TestCase):

    def testMutiplication(self):
           
        five = Dollar.Dollar(5)
        
        product = five.times(2)
        self.assertEqual(10, product.amount)

        product = five.times(3)
        self.assertEqual(15, product.amount)

    def testEquality(self):
        self.assertTrue(Dollar.Dollar(5).equals(Dollar.Dollar(5)))
        self.assertFalse(Dollar.Dollar(5).equals(Dollar.Dollar(6)))

if __name__ == '__main__':
    unittest.main()