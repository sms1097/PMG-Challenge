from src.out_of_memory_combine import out_of_memory_combine
from src.in_memory_combine import in_memory_combine
from src.combine import combine
import pandas as pd
import unittest


class CombineTests(unittest.TestCase):

    def test_all_equal(self):
        basic = pd.read_csv('model_outputs/basic_combine.csv')
        inm = pd.read_csv('model_outputs/inm_combine.csv')
        oom = pd.read_csv('model_outputs/oom_combine.csv')

        self.assertTrue(basic.equals(inm))
        self.assertTrue(inm.equals(oom))


if __name__ == '__main__':
    unittest.main()