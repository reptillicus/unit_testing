from unittest import TestCase
from example1.fizzbuzz import fizbuzz

class FizzBuzzTest(TestCase):
    """
    A dead simple example of unit testing the fizzbuzz function
    """
    def setUp(self):
        print('setup')

    def tearDown(self):
        pass

    def test_fizz(self):
        res = fizbuzz(3)
        self.assertTrue(res == "fizz")

        res = fizbuzz(5)
        self.assertTrue(res == "buzz")

        res = fizbuzz(15)
        # asssert with a more informative message
        self.assertTrue(res == "fizzbuzz", "Should be fizzbuzz for 15")

