import unittest

class CheckUnitTesting(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(3,sum([1,2]))

    def test_simple_2(self):
        self.assertEqual(4,sum([1,3]))

if __name__ == '__main__':
    unittest.main()
