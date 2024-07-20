from tests import *




class TestExceptions(unittest.TestCase):
    def test_invalid_json(self):
        with self.assertRaises(ValueError) as context: 
            repair_json('hello')
        self.assertEqual(str(context.exception), 'Invalid JSON string')