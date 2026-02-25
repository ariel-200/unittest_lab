import unittest 
from unittest import TestCase
from cart_discount.price_discount import discount

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))
    
    # More unit tests here. Each test should test one scenario

    def test_list_of_four_prices(self):
        prices = [10, 4, 20, 100]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_empty_list(self):
        prices = []
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_one_price(self):
        prices = [1]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_two_prices(self):
        prices = [2, 4]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_discount_non_numeric(self):
        prices = [10, "hello", 5]
        with self.assertRaises(TypeError):
            discount(prices)

    def test_negative_numbers(self):
        prices = [-1, -2, -8]
        expected_discount = -8
        self.assertEqual(expected_discount, discount(prices))

    def test_all_strings(self):
        prices = ["10", "5", "20"]
        expected_discount = "10"
        self.assertEqual(expected_discount, discount(prices))

    def test_mixed_numbers(self):
        prices = [10, -2, 2.58]
        expected_discount = -2
        self.assertEqual(expected_discount, discount(prices))

    def test_list_None(self):
        prices = None
        with self.assertRaises(TypeError):
            discount(prices)

    def test_list_with_None(self):
        prices = [10, None, 5]
        with self.assertRaises(TypeError):
            discount(prices)

    def test_all_three_same_price(self):
        prices = [10, 10, 10]
        expected_discount = 10
        self.assertEqual(expected_discount, discount(prices))

    def test_list_very_large_numbers(self):
        prices = [1000000000000000000000000000000000000, 200000000000000000000000000000000000,
                  3000000000000000000000000000000000000000000000000000000]
        expected_discount = 200000000000000000000000000000000000
        function_returned_discount = discount(prices)
        self.assertEqual(expected_discount, function_returned_discount)

    def test_list_of_floats(self):
        prices = [10.99, 5.99, 20.99]
        expected_discount = 5.99
        function_returned_discount = discount(prices)
        self.assertEqual(expected_discount, function_returned_discount)

    def test_list_of_zeros(self):
        prices = [0, 0, 0]
        expected_discount = 0
        function_returned_discount = discount(prices)
        self.assertEqual(expected_discount, function_returned_discount)

    def test_list_with_zero_and_positive_numbers(self):
        prices = [0, 10, 20]
        expected_discount = 0
        function_returned_discount = discount(prices)
        self.assertEqual(expected_discount, function_returned_discount)

    def test_with_one_negative_number(self):
        prices = [10, -5, 20]
        expected_discount = -5
        function_returned_discount = discount(prices)
        self.assertEqual(expected_discount, function_returned_discount)

    def test_with_mixed_numbers_and_zero(self):
        prices = [0, -5, 10]
        expected_discount = -5
        function_returned_discount = discount(prices)
        self.assertEqual(expected_discount, function_returned_discount)

    def test_with_multiple_smallest_numbers(self):
        prices = [10, 5, 5, 20]
        expected_discount = 5
        function_returned_discount = discount(prices)
        self.assertEqual(expected_discount, function_returned_discount)

    def test_with_large_negative_numbers(self):
        prices = [-1000000000000000000, -2000000000000, -3000000]
        expected_discount = -1000000000000000000
        function_returned_discount = discount(prices)
        self.assertEqual(expected_discount, function_returned_discount)

    def test_large_numbers_but_not_enough_items(self):
        prices = [1000000000000000000, 2000000000000]
        expected_discount = 0
        function_returned_discount = discount(prices)
        self.assertEqual(expected_discount, function_returned_discount)

    def test_list_of_strings_but_not_enough_items(self):
        prices = ["10", "5"]
        expected_discount = 0
        function_returned_discount = discount(prices)
        self.assertEqual(expected_discount, function_returned_discount)

    def test_string_instead_of_list(self):
        prices = "Testing String"
        expected_discount = ' '
        function_returned_discount = discount(prices)
        self.assertEqual(expected_discount, function_returned_discount)

    def test_dictionary_instead_of_list(self):
        prices = {"item1": 10, "item2": 5, "item3": 20}
        expected_discount = 'item1'
        function_returned_discount = discount(prices)
        self.assertEqual(expected_discount, function_returned_discount)

    def test_tuple_instead_of_list(self):
        prices = (10, 7, 8)
        expected_discount = 7
        function_returned_discount = discount(prices)
        self.assertEqual(expected_discount, function_returned_discount)

if __name__ == '__main__':
    unittest.main()