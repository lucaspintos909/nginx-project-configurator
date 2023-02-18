import unittest

from validators import domains_validator


class RpgTestCase(unittest.TestCase):

    def test_generator_success(self):
        result = domains_validator(["example.com", "www.example.com"])
        self.assertTrue(result["valid"])
        self.assertEqual(len(result["message"]), 0)

        result = domains_validator(["www.example.com", "example.com"])
        self.assertTrue(result["valid"])
        self.assertEqual(len(result["message"]), 0)

    def test_generator_error(self):
        result = domains_validator(["example.com", "example.com"])
        self.assertFalse(result["valid"])
        self.assertGreater(len(result["message"]), 0)
        
        result = domains_validator(["example.com", "test.example.com"])
        self.assertFalse(result["valid"])
        self.assertGreater(len(result["message"]), 0)
        
        result = domains_validator(["example.com"])
        self.assertFalse(result["valid"])
        self.assertGreater(len(result["message"]), 0)
        
        result = domains_validator(["example.com", "www.example.com", "test.example.com"])
        self.assertFalse(result["valid"])
        self.assertGreater(len(result["message"]), 0)
