import unittest
from solution import *

with open('expected_output.txt', 'r') as file:
    expected = file.read()

class TopSellerTest(unittest.TestCase):
    def test_solution_with_the_given_case(self):
        result = generate_top_sellers_report(min_date="2020-02-01", max_date="2020-06-30", top=2)
        self.assertEquals(result, expected)



if __name__ == '__main__':
    unittest.main()
