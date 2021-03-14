import unittest

# テストをしたいモジュールをimportする
import Dollar
import Franc

# クラス名はなんでもよいが、unittest.TestCaseの継承は必要
class MoneyTest(unittest.TestCase):

    def testMutiplication(self):
           
        five = Dollar.Dollar(5)
        ten = Dollar.Dollar(10)
        fifth = Dollar.Dollar(15)

        # オブジェクト同士の比較はうまくいかない
        self.assertEqual(ten.amount, five.times(2).amount)
        # オブジェクト同士の比較はうまくいかない
        self.assertEqual(fifth.amount, five.times(3).amount)

    def testEquality(self):
        self.assertTrue(Dollar.Dollar(5).equals(Dollar.Dollar(5)))
        self.assertFalse(Dollar.Dollar(5).equals(Dollar.Dollar(6)))
    
    def testFrancMultiplication(self):
        five = Franc.Franc(5)
        ten = Franc.Franc(10)
        fifth = Franc.Franc(15)

        self.assertEqual(ten.amount, five.times(2).amount)
        self.assertEqual(fifth.amount, five.times(3).amount)

if __name__ == '__main__':
    unittest.main()