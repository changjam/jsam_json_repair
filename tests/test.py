import unittest
from json_repair import repair_json




class TestJsonRepair(unittest.TestCase):
    def test_basic_types_valid(self):
        self.assertEqual(repair_json('{"test": 123}'), {"test": 123})


class TestExceptions(unittest.TestCase):
    def test_invalid_json(self):
        with self.assertRaises(ValueError) as context: 
            repair_json('hello')
        self.assertEqual(str(context.exception), 'Invalid JSON string')