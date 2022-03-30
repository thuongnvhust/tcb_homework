import unittest
from module import validation


class TestingValidation(unittest.TestCase):
    def test_insert(self):
        input_true = {
           "poolId": 123546,
           "poolValues": [1, 7, 2, 6]
        }
        input_true_ex = validation.validate_new_pool(pool=input_true)
        self.assertIsInstance(input_true_ex, Exception)

        input_false = {
           "poolId": 123546,
           "poolValues": [1, 7, 2, '5']
        }
        input_false_ex = validation.validate_new_pool(pool=input_false)
        self.assertIsInstance(input_false_ex, Exception)


if __name__ == '__main__':
    unittest.main()