import unittest

from pyvalidator import *


class TestIsIban(unittest.TestCase):
	def valid_check(self, items, country_code = None, options = {}):
		for item in items:
			try:
				self.assertTrue(is_iban(item, country_code, options))
			except Exception as e:
				print(f'failed for input: {item}')
				raise e

	def invalid_check(self, items, country_code = None, options = {}):
		for item in items:
			try:
				self.assertFalse(is_iban(item, country_code, options))
			except Exception as e:
				print(f'failed for input: {item}')
				raise e

	def test_valid_iban(self):
		valid = [
			'AD12 0001 2030 2003 5910 0100',
			'AD1200012030200359100100',
			'DE89370400440532013000',
			'HU42117730161111101800000000',
			'FR14 2004 1010 0505 0001 3M02 606',
			'ES9121000418450200051332',
			'UA213223130000026007233566001',
			'NO93 8601 1117 947',
			'RS35 2600 0560 1001 6113 79',
			'GB29 NWBK 6016 1331 9268 19',
			'SE4550000000058398257466',
			'BE68 5390 0754 7034',
			'HR1210010051863000160',
			'HR 1210010051863000160',
			'EE38 2200 2210 2014 5682',
			'BA39 1290 07940102 8494',
			'IL620108000000099999999',
			'GR16 0110 1250 0000 0001 2300 695',
			' GR16 0110 1250 0000 0001 2300 695 ',
			' PL61109010140000071219812874',
			'TR330006100519786457841326',
			'MK07 250A 2000 0058 984',
			'MK07 2501 2000 0058 A84',
			'AL47212110090000000235698741',
			'AZ21NABZ00000000137010001944',
			'MT84MALT011000012345MTLCAST001S',
			'PT50000201231234567890154',
			'AT483200000012345864',
			'LU280019400644750000',
			'LU28001A400644750000',
			'CY17002001280000001200527600',
			'DO22ACAU00000000000123456789',
			'DO22AC1U00000000000123456789',
			'IT60X0542811101000000123456',
			'KW81CBKU0000000000001234560101',
			'LT121000011101001000',
			'FI2112345600000785',
			'LV80BANK0000435195001',
			'MD24AG000225100013104168',
			'RO49AAAA1B31007593840000',
			'ME25505000012345678951',
		]
		self.valid_check(valid)
		print('OK - test_valid_iban')

	def test_invalid_iban(self):
		invalid = [
			'AD12 0001 2030 2003 5910 01001',
			'HU421177301611111018000000001',
			'FR14 2004 1010 0505 000 3M02 606',
			'ES912000418450200051332',
			'UAA213223130000026007233566001',
			'NO93 8601 117 947',
			'RS35 063 0560 1001 6113 79',
			'GB29 NWBKA 6016 1331 9268 19',
			'GB29 NWB 6016 1331 9268 19',
			'SE45500000000583982574A6',
			'BE68 5390 0754',
			'BE68 5390 0754 7034 1111',
			'HR121001005186300016',
			'EE38 2200 2210 2014',
			'E38 2200 2210 2014',
			'IL62010800000009999999#',
			'IL62010800000009999999',
			'IL62010800000009999999a',
			'GR16 0110 12$0 0000 0001 2300 695',
			'PL6110901014000007121981287A',
			'PL611090101400000712198128755',
			'TR330A06100519786457841326',
			'TR33000610051978645784132#',
			'MK07 2501 200# 0058 984#',
			'MK07 2501 2000 0058 A8A',
			'AL472121100A0000000235698741',
			'AL472121100100000002#5698741',
			'AZDDNABZ00000000137010001944',
			'AZ21NAB100000000137010001944',
			'MT8AMALT011000012345MTLCAST001S',
			'MT82MAL4011000012345MTLCAST001S',
			'MT82MALB01A000012345MTLCAST001S',
			'MT82MALB011000012345MTLC$ST001S',
			'PT500002012312345678901542',
			'PT5000020123123456789015',
			'PT5000020123123456789015A',
			'AT48320000001234586',
			'AT4832000000123458644',
			'AT48320000001234586A',
			'LU2800A9400644750000',
			'LU28001@400644750000',
			'CY170020012A0000001200527600',
			'CY170020012810000001200527600',
			'DO2AACAU00000000000123456789',
			'DO22ACAUA0000000000123456789',
			'DO22ACAU000000000001234567899',
			'IT6010542811101000000123456',
			'IT6XX0542811101000000123456',
			'IT61X054281110A000000123456',
			'KW8ACBKU0000000000001234560101',
			'KW81CBK10000000000001234560101',
			'KW81CBKA10000000000001234560101',
			'LT12100001110100100A',
			'LT1210000111010010001',
			'FI211234560000078A',
			'LV8ABANK0000435195001',
			'LV81BAN10000435195001',
			'LV81BANK00004351950012',
			'MDA4AG000225100013104168',
			'MD$4AG0002251000131041681',
			'RO49AAA11B31007593840000',
			'RO1AAAAA1B31007593840000',
			'ME2550500001234567895A',
			'XX2550500001234567895A',
			'me25505000012345678951',
			'ch9300762011623852957'
		]
		self.invalid_check(invalid)
		print('OK - test_invalid_iban')

	def test_valid_iban_DE(self):
		valid = [
			'DE89370400440532013000',
			'89370400440532013000',
		]
		self.valid_check(valid, 'DE')
		print('OK - test_valid_iban_DE')

	def test_invalid_iban_DE(self):
		invalid = [
			'DE189370400440532013000',
			'819370400440532013000',
		]
		self.invalid_check(invalid, 'DE')
		print('OK - test_invalid_iban_DE')

	def test_valid_iban_IT(self):
		valid = [
			'IT60X0542811101000000123456',
			'60X0542811101000000123456',
			' 60X0542811101000000123456',
		]
		self.valid_check(valid, 'IT')
		print('OK - test_valid_iban_IT')

	def test_valid_iban_IT_lc(self):
		valid = [
			'IT60X0542811101000000123456',
			'60X0542811101000000123456',
			' 60X0542811101000000123456',
		]
		self.valid_check(valid, 'it')
		print('OK - test_valid_iban_IT_lc')

	def test_invalid_iban_IT(self):
		invalid = [
			'IT61X054281110A000000123456',
			'61X054281110A000000123456',
		]
		self.invalid_check(invalid, 'IT')
		print('OK - test_invalid_iban_IT')

	def test_valid_iban_MT(self):
		valid = [
			'MT84MALT011000012345MTLCAST001S',
			'84MALT011000012345MTLCAST001S',
		]
		self.valid_check(valid, 'MT')
		print('OK - test_valid_iban_MT')

	def test_invalid_iban_MT(self):
		invalid = [
			'MT82MALB01A000012345MTLCAST001S',
			'DE89370400440532013000',
			'60X0542811101000000123456'
		]
		self.invalid_check(invalid, 'MT')
		print('OK - test_invalid_iban_MT')

	def test_invalid_iban_unknown_country_code(self):
		invalid = [
			'MT84MALT011000012345MTLCAST001S',
			'DE89370400440532013000',
			'60X0542811101000000123456'
		]
		self.invalid_check(invalid, 'XX')
		print('OK - test_invalid_iban_unknown_country_code')


	def test_valid_iban_case_insensitive(self):
		valid = [
			'rs35 2600 0560 1001 6113 79',
			'gb29 nwbk 6016 1331 9268 19',
			'ch9300762011623852957',
			'sI 56263300012039086'
		]
		self.valid_check(valid, options = { "insensitive": True })
		print('OK - test_valid_iban_case_insensitive')
