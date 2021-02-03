import sys
import unittest
from io import StringIO
from src.combine import combine
import pandas as pd


class CombineTests(unittest.TestCase):

    def test_all_equal(self):
        basic = pd.read_csv('model_outputs/basic_combine.csv')
        inm = pd.read_csv('model_outputs/inm_combine.csv')
        oom = pd.read_csv('model_outputs/oom_combine.csv')

        self.assertTrue(basic.equals(inm))
        self.assertTrue(inm.equals(oom))

    def test_static_file1(self):
        result = pd.read_csv('model_outputs/stat_test1.csv')
        test1 = pd.read_csv('test_files/test1.csv')
        self.assertTrue(test1.equals(result))

    def test_static_file2(self):
        result = pd.read_csv('model_outputs/stat_test2.csv')
        test1 = pd.read_csv('test_files/test2.csv')
        self.assertTrue(test1.equals(result))


if __name__ == '__main__':
    unittest.main()
