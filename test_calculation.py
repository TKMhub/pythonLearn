import unittest

import calculation

class CalTest(unittest.TestCase):
    def test_add_num_and_double(self):
        cal = calculation.Cal()
        self.assertEqual(cal.add_num_and_double(1, 1),4)


# コマンドラインからの実行メソッド
if __name__ == '__main__':
    unittest.main()