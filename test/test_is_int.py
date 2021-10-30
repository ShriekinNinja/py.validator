import unittest
import validator

class TestIsInt(unittest.TestCase):

    def test_valid_ints(self):
        self.assertTrue(validator.is_int('13'))
        self.assertTrue(validator.is_int('123'))
        self.assertTrue(validator.is_int('0'))
        self.assertTrue(validator.is_int('-0'))
        self.assertTrue(validator.is_int('+1'))
        self.assertTrue(validator.is_int('01'))
        self.assertTrue(validator.is_int('-01'))
        self.assertTrue(validator.is_int('000'))
        print('OK - test_valid_ints')

    def test_invalid_ints(self):
        self.assertFalse(validator.is_int('100e10'))
        self.assertFalse(validator.is_int('123.123'))
        self.assertFalse(validator.is_int('   '))
        self.assertFalse(validator.is_int(''))
        self.assertFalse(validator.is_int('.'))
        self.assertFalse(validator.is_int('foo'))
        print('OK - test_invalid_ints')

    def test_valid_ints_dont_allow_leading_zeroes(self) -> bool:
        self.assertTrue(validator.is_int('13', { "allow_leading_zeroes": False }))
        self.assertTrue(validator.is_int('11', { "allow_leading_zeroes": False }))
        self.assertTrue(validator.is_int('123', { "allow_leading_zeroes": False }))
        self.assertTrue(validator.is_int('0', { "allow_leading_zeroes": False }))
        self.assertTrue(validator.is_int('-0', { "allow_leading_zeroes": False }))
        self.assertTrue(validator.is_int('+1', { "allow_leading_zeroes": False }))
        print('OK - test_valid_ints_dont_allow_leading_zeroes')

    def test_invalid_ints_dont_allow_leading_zeroes(self):
        self.assertFalse(validator.is_int('01', { "allow_leading_zeroes": False }))
        self.assertFalse(validator.is_int('-01', { "allow_leading_zeroes": False }))
        self.assertFalse(validator.is_int('000', { "allow_leading_zeroes": False }))
        self.assertFalse(validator.is_int('100e10', { "allow_leading_zeroes": False }))
        self.assertFalse(validator.is_int('123.11', { "allow_leading_zeroes": False }))
        self.assertFalse(validator.is_int('foo', { "allow_leading_zeroes": False }))
        self.assertFalse(validator.is_int('   ', { "allow_leading_zeroes": False }))
        self.assertFalse(validator.is_int('', { "allow_leading_zeroes": False }))
        self.assertFalse(validator.is_int('\n', { "allow_leading_zeroes": False }))
        self.assertFalse(validator.is_int('\t', { "allow_leading_zeroes": False }))
        print('OK - test_invalid_ints_dont_allow_leading_zeroes')
