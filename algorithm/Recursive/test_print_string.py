import unittest


class TestDisplayString(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
    DisplayString.forward_iter_way("This is test string")
    DisplayString.forward_recursive_way("This is test string")
