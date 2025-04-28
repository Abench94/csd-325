import unittest
from city_functions import catLocations

class TestCityFunctions(unittest.TestCase):

    def test_city_country(self):
        destination = catLocations("santiago", "chile")
        self.assertEqual(destination, "Santiago, Chile")

if __name__ == '__main__':
    unittest.main()
    