import unittest
from conversions import (
    convertCelsiusToKelvin, convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius, convertFahrenheitToKelvin,
    convertKelvinToCelsius, convertKelvinToFahrenheit
)

class TestTemperatureConversions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        """Test conversion from Celsius to Kelvin"""
        test_cases = [
            (0, 273.15),
            (100, 373.15),
            (-273.15, 0),  # Absolute zero
            (300, 573.15),
            (-40, 233.15)
        ]
        for celsius, expected_kelvin in test_cases:
            with self.subTest(celsius=celsius, expected_kelvin=expected_kelvin):
                self.assertAlmostEqual(convertCelsiusToKelvin(celsius), expected_kelvin, places=2)

    def test_convertCelsiusToFahrenheit(self):
        """Test conversion from Celsius to Fahrenheit"""
        test_cases = [
            (0, 32),
            (100, 212),
            (-40, -40),
            (300, 572),
            (-273.15, -459.67)  # Absolute zero
        ]
        for celsius, expected_fahrenheit in test_cases:
            with self.subTest(celsius=celsius, expected_fahrenheit=expected_fahrenheit):
                self.assertAlmostEqual(convertCelsiusToFahrenheit(celsius), expected_fahrenheit, places=2)

    def test_convertFahrenheitToCelsius(self):
        """Test conversion from Fahrenheit to Celsius"""
        test_cases = [
            (32, 0),
            (212, 100),
            (-40, -40),
            (572, 300),
            (-459.67, -273.15)  # Absolute zero
        ]
        for fahrenheit, expected_celsius in test_cases:
            with self.subTest(fahrenheit=fahrenheit, expected_celsius=expected_celsius):
                self.assertAlmostEqual(convertFahrenheitToCelsius(fahrenheit), expected_celsius, places=2)

    def test_convertFahrenheitToKelvin(self):
        """Test conversion from Fahrenheit to Kelvin"""
        test_cases = [
            (32, 273.15),
            (212, 373.15),
            (-40, 233.15),
            (572, 573.15),
            (-459.67, 0)  # Absolute zero
        ]
        for fahrenheit, expected_kelvin in test_cases:
            with self.subTest(fahrenheit=fahrenheit, expected_kelvin=expected_kelvin):
                self.assertAlmostEqual(convertFahrenheitToKelvin(fahrenheit), expected_kelvin, places=2)

    def test_convertKelvinToCelsius(self):
        """Test conversion from Kelvin to Celsius"""
        test_cases = [
            (273.15, 0),
            (373.15, 100),
            (0, -273.15),
            (573.15, 300),
            (233.15, -40)
        ]
        for kelvin, expected_celsius in test_cases:
            with self.subTest(kelvin=kelvin, expected_celsius=expected_celsius):
                self.assertAlmostEqual(convertKelvinToCelsius(kelvin), expected_celsius, places=2)

    def test_convertKelvinToFahrenheit(self):
        """Test conversion from Kelvin to Fahrenheit"""
        test_cases = [
            (273.15, 32),
            (373.15, 212),
            (0, -459.67),
            (573.15, 572),
            (233.15, -40)
        ]
        for kelvin, expected_fahrenheit in test_cases:
            with self.subTest(kelvin=kelvin, expected_fahrenheit=expected_fahrenheit):
                self.assertAlmostEqual(convertKelvinToFahrenheit(kelvin), expected_fahrenheit, places=2)

if __name__ == '__main__':
    unittest.main()