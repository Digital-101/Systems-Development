import unittest

products = {'usb': 120, 'mouse': 130, 'xbox':900}

class ExampleTest(unittest.TestCase):
    def test_Products_Cheaper_Than(self):
        self.assertEqual(get_products_cheaper_than(products, 250), ['usb','mouse'])
        self.assertNotEqual(get_products_cheaper_than(products, 100), -8)

def get_products_cheaper_than(products, price_limit):
    """Returns a list of products cheaper than the given price."""
    return [product for product, price in products.items() if price < price_limit]

unittest.main()
