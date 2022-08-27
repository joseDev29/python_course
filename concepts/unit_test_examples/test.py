import unittest

from code_to_test import string_to_uppercase


class TestCodeToUppercase(unittest.TestCase):

    # all testing functions must begin with the word test
    def test_uppercase(self):
        word = 'hello world'
        result = string_to_uppercase('HELLO WORLD')
        self.assertEqual(result, 'HELLO WORLD')


if __name__ == '__main__':
    unittest.main()
