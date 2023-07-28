import unittest

import calculation

class CalTest(unittest.TestCase):
    # テスト開始時に実行される
    def setUp(self):
        print('setUp')
        self.cal = calculation.Cal()

    def tearDown(self):
        print('clean up')
        del self.cal


    def test_add_num_and_double(self):
        cal = calculation.Cal()
        self.assertEqual(cal.add_num_and_double(1, 1),4)

    def test_add_num_and_double_raise(self):
        cal = calculation.Cal()
        with self.assertRaises(ValueError):
            cal.add_num_and_double('1', '1')


# コマンドラインからの実行メソッド
if __name__ == '__main__':
    unittest.main()