import unittest


class CheckUnitTesting(unittest.TestCase):
    def simple_test(self):
        self.assertEqual(3,sum([1,2]))

    def simple_test_2(self):
        self.assertEqual(4,sum([1,4]))

if __name__ == '__main__':
    unittest.main()
