import unittest
from solution import *


class TopSellerTest(unittest.TestCase):
    def test_solution_with_the_given_case(self):
        result = get_top_sellers_report(min_date="2020-02-01", max_date="2020-06-30", top=2)
        self.assertEqual(result,
"-- top seller product --\
  name  quantity\
 p-103        33\
 p-102        24\
 p-110        24\
-- top seller store --\
name  quantity\
 s-3        42\
 s-2        36\
 s-7        36\
-- top seller brand --\
    brand  quantity\
 yoyodyne       100\
     acme        65\
-- top seller city --\
      city  quantity\
    gotham       108\
 coruscant        78")



if __name__ == '__main__':
    unittest.main()
