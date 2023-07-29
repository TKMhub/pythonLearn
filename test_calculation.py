# import unittest
import pytest

import calculation

# pytest
# def test_add_num_and_double():
#     cal = calculation.Cal()
#     # assert cal.add_num_and_double(1,1) == 4
#     # assert cal.add_num_and_double(1,1) in 4
#     assert cal.add_num_and_double(1,1) != 4


class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()

    @classmethod
    def teardown_class(cls):
        cls.cal

    def setup_method(self, method):
        print('method={}'.format(method.__name__))
        self.cal = calculation.Cal()

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
        self.cal = calculation.Cal()


    def test_add_num_and_double(self):
        cal = calculation.Cal()
        assert cal.add_num_and_double(1,1) == 4

    # 例外処理のテスト
    # def test_add_num_and_double_raise(self):
    #     with pytest.raises(ValueError):
    #         cal = calculation.Cal()
    #         cal.cal.add_num_and_double('1', '1')

#Unitテスト

# import calculation
#
# release_name = 'lesson'
#
# class CalTest(unittest.TestCase):
#     # テスト開始時に実行される
#     def setUp(self):
#         print('setUp')
#         self.cal = calculation.Cal()
#
#     def tearDown(self):
#         print('clean up')
#         del self.cal
#
#     # @unittest.skip('skip!')
#     @unittest.skipIf(release_name=='lesson', 'skip!')
#     def test_add_num_and_double(self):
#         cal = calculation.Cal()
#         self.assertEqual(cal.add_num_and_double(1, 1),4)
#
#     def test_add_num_and_double_raise(self):
#         cal = calculation.Cal()
#         with self.assertRaises(ValueError):
#             cal.add_num_and_double('1', '1')


# コマンドラインからの実行メソッド
if __name__ == '__main__':
    unittest.main()