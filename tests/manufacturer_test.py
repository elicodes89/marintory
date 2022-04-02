import unittest

from models.manufacturer import Manufacturer

if __name__ == '__main__':
    unittest.main()

class TestManufacturer(unittest.TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer("AKA Reef" , "aka@reef.com" , "0131 222 3333" , "live stock")

    def test_manufacturer_has_name(self):
        self.assertEqual("AKA Reef" , self.manufacturer.name)