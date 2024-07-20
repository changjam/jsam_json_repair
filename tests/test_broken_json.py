from tests import *



class TestBrokenJson(unittest.TestCase):
    def test_lack_of_comma(self):
        self.assertEqual(repair_json(ERROR_FORMAT1), CORRECT_FORMAT1)

    def test_redundant_comma_at_the_end(self):
        self.assertEqual(repair_json(ERROR_FORMAT2), CORRECT_FORMAT2)

    def test_missing_quotation_marks(self):
        self.assertEqual(repair_json(ERROR_FORMAT3_1), CORRECT_FORMAT3_1)
        self.assertEqual(repair_json(ERROR_FORMAT3_2), CORRECT_FORMAT3_2)
        self.assertEqual(repair_json(ERROR_FORMAT3_3), CORRECT_FORMAT3_3)
        self.assertEqual(repair_json(ERROR_FORMAT3_4), CORRECT_FORMAT3_4)

    def test_missing_parentheses(self):
        self.assertEqual(repair_json(ERROR_FORMAT4), CORRECT_FORMAT4)

    def test_error_boolean_value(self):
        self.assertEqual(repair_json(ERROR_FORMAT5), CORRECT_FORMAT5)

    def test_error_apostrophe(self):
        self.assertEqual(repair_json(ERROR_FORMAT6), CORRECT_FORMAT6)

    def test_error_none(self):
        self.assertEqual(repair_json(ERROR_FORMAT7), CORRECT_FORMAT7)