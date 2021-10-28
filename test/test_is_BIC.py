import unittest
import validator

class TestIsBIC(unittest.TestCase):

    def test_valid_bic_codes(self) -> bool:
        self.assertTrue(validator.is_BIC('SBICKEN1345'))
        self.assertTrue(validator.is_BIC('SBICKEN1'))
        self.assertTrue(validator.is_BIC('SBICKENY'))
        self.assertTrue(validator.is_BIC('SBICKEN1YYP'))
        print('OK - test_valid_bic_codes')

    def test_invalid_bic_codes(self):
        self.assertFalse(validator.is_BIC('SBIC23NXXX'))
        self.assertFalse(validator.is_BIC('S23CKENXXXX'))
        self.assertFalse(validator.is_BIC('SBICKENXX'))
        self.assertFalse(validator.is_BIC('SBICKENXX9'))
        self.assertFalse(validator.is_BIC('SBICKEN13458'))
        self.assertFalse(validator.is_BIC('SBICKEN'))
        print('OK - test_invalid_bic_codes')
