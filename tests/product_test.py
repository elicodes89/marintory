import unittest

from models.product import Product
from models.store import Store

if __name__ == '__main__':
    unittest.main()

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("Clown Fish" , "live stock" , 20 , 25)
        self.product2 = Product("Flakes" , "food" , 3 , 7 ) 
        self.product3 = Product("Thermometer" , "accessories" , 10 , 25 )

        self.store = Store("Grow Coral")

    def test_product_has_cost_price(self):
        self.assertEqual(20 , self.product.cost)

    def test_add_product(self):
        self.store.add_product(self.product2)
        self.assertEqual(1, self.store.products_count(self.store.products))

    
        