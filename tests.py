import conversion
import unittest


class TempConversionValues(unittest.TestCase):

    test_values_c_to_k = [(100, 373.15),
                          (500, 773.15),
                          (115.75, 388.9),
                          (321.5, 594.65),
                          (0.05, 273.2)]

    test_values_c_to_f = [(100, 212),
                          (500, 932),
                          (115.75, 240.35),
                          (321.5, 610.7),
                          (0.05, 32.09)]

    test_values_f_to_c = [(100, 37.7778),
                          (500, 260),
                          (115.75, 46.5278),
                          (321.5, 160.8333),
                          (0.05, -17.75)]

    test_values_f_to_k = [(100, 310.9278),
                          (500, 533.15),
                          (115.75, 319.6778),
                          (321.5, 433.9833),
                          (0.05, 255.4)]

    test_values_k_to_c = [(100, -173.15),
                          (500, 226.85),
                          (115.75, -157.4),
                          (321.5, 48.35),
                          (0.05, -273.1)]

    test_values_k_to_f = [(100, -279.67),
                          (500, 440.33),
                          (115.75, -251.32),
                          (321.5, 119.03),
                          (0.05, -459.58)]

    def test_celsius_to_kelvin_conversion(self):
        for val, res in self.test_values_c_to_k:
            conv_c_to_k_res = conversion.convert_celsius_to_kelvin(val)
            self.assertEqual(res, conv_c_to_k_res)
            print(f"Test for converting {val} celsius to {res:.2f} kelvin passed")

    def test_celsius_to_fahrenheit_conversion(self):
        for val, res, in self.test_values_c_to_f:
            conv_c_to_f_res = conversion.convert_celsius_to_fahrenheit(val)
            self.assertEqual(res, conv_c_to_f_res)
            print(f"Test for converting {val} celsius to {res:.2f} fahrenheit passed")

    def test_fahrenheit_to_celsius_conversion(self):
        for val, res, in self.test_values_f_to_c:
            conv_f_to_c_res = conversion.convert_fahrenheit_to_celsius(val)
            self.assertEqual(res, conv_f_to_c_res)
            print(f"Test for converting {val} fahrenheit to {res:.2f} celsius passed")

    def test_fahrenheit_to_kelvin_conversion(self):
        for val, res, in self.test_values_f_to_k:
            conv_f_to_k_res = conversion.convert_fahrenheit_to_kelvin(val)
            self.assertEqual(res, conv_f_to_k_res)
            print(f"Test for converting {val} fahrenheit to {res:.2f} kelvin passed")

    def test_kelvin_to_celsius_conversion(self):
        for val, res, in self.test_values_k_to_c:
            conv_k_to_c_res = conversion.convert_kelvin_to_celsius(val)
            self.assertEqual(res, conv_k_to_c_res)
            print(f"Test for converting {val} kelvin to {res:.2f} celsius passed")

    def test_kelvin_to_fahrenheit_conversion(self):
        for val, res, in self.test_values_k_to_f:
            conv_k_to_f_res = conversion.convert_kelvin_to_fahrenheit(val)
            self.assertEqual(res, conv_k_to_f_res)
            print(f"Test for converting {val} kelvin to {res:.2f} fahrenheit passed")


if __name__ == '__main__':
    unittest.main()
