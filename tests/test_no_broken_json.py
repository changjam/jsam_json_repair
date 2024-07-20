from tests import *




class TestNoBrokenJson(unittest.TestCase):
    def test_basic_types_int_valid(self):
        self.assertEqual(repair_json('{"test": 123}'), {"test": 123})

    def test_basic_types_str_valid(self):
        self.assertEqual(repair_json('{"hello": "world"}'), {"hello": "world"})

    def test_basic_types_bool_valid(self):
        self.assertEqual(repair_json('{"is_success": true}'), {"is_success": True})