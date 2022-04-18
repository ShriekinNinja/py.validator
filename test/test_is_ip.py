import unittest

from pyvalidator import *


class TestIsIp(unittest.TestCase):

    def test_valid_ip(self) -> bool:
        self.assertTrue(is_ip('127.0.0.1'))
        self.assertTrue(is_ip('0.0.0.0'))
        self.assertTrue(is_ip('255.255.255.255'))
        self.assertTrue(is_ip('1.2.3.4'))
        self.assertTrue(is_ip('::1'))
        self.assertTrue(is_ip('2001:db8:0000:1:1:1:1:1'))
        self.assertTrue(is_ip('2001:db8:3:4::192.0.2.33'))
        self.assertTrue(is_ip('2001:41d0:2:a141::1'))
        self.assertTrue(is_ip('::ffff:127.0.0.1'))
        self.assertTrue(is_ip('::0000'))
        self.assertTrue(is_ip('0000::'))
        self.assertTrue(is_ip('1::'))
        self.assertTrue(is_ip('1111:1:1:1:1:1:1:1'))
        self.assertTrue(is_ip('fe80::a6db:30ff:fe98:e946'))
        self.assertTrue(is_ip('::'))
        self.assertTrue(is_ip('::8'))
        self.assertTrue(is_ip('::ffff:127.0.0.1'))
        self.assertTrue(is_ip('::ffff:255.255.255.255'))
        self.assertTrue(is_ip('::ffff:0:255.255.255.255'))
        self.assertTrue(is_ip('::2:3:4:5:6:7:8'))
        self.assertTrue(is_ip('::255.255.255.255'))
        self.assertTrue(is_ip('0:0:0:0:0:ffff:127.0.0.1'))
        self.assertTrue(is_ip('1:2:3:4:5:6:7::'))
        self.assertTrue(is_ip('1:2:3:4:5:6::8'))
        self.assertTrue(is_ip('1::7:8'))
        self.assertTrue(is_ip('1:2:3:4:5::7:8'))
        self.assertTrue(is_ip('1:2:3:4:5::8'))
        self.assertTrue(is_ip('1::6:7:8'))
        self.assertTrue(is_ip('1:2:3:4::6:7:8'))
        self.assertTrue(is_ip('1:2:3:4::8'))
        self.assertTrue(is_ip('1::5:6:7:8'))
        self.assertTrue(is_ip('1:2:3::5:6:7:8'))
        self.assertTrue(is_ip('1:2:3::8'))
        self.assertTrue(is_ip('1::4:5:6:7:8'))
        self.assertTrue(is_ip('1:2::4:5:6:7:8'))
        self.assertTrue(is_ip('1:2::8'))
        self.assertTrue(is_ip('1::3:4:5:6:7:8'))
        self.assertTrue(is_ip('1::8'))
        self.assertTrue(is_ip('fe80::7:8%eth0'))
        self.assertTrue(is_ip('fe80::7:8%1'))
        self.assertTrue(is_ip('64:ff9b::192.0.2.33'))
        self.assertTrue(is_ip('0:0:0:0:0:0:10.0.0.1'))
        print('OK - test_valid_ip')

    def test_invalid_ip(self):
        self.assertFalse(is_ip('abc'))
        self.assertFalse(is_ip('256.0.0.0'))
        self.assertFalse(is_ip('0.0.0.256'))
        self.assertFalse(is_ip('26.0.0.256'))
        self.assertFalse(is_ip('0200.200.200.200'))
        self.assertFalse(is_ip('200.0200.200.200'))
        self.assertFalse(is_ip('200.200.0200.200'))
        self.assertFalse(is_ip('200.200.200.0200'))
        self.assertFalse(is_ip('::banana'))
        self.assertFalse(is_ip('banana::'))
        self.assertFalse(is_ip('::1banana'))
        self.assertFalse(is_ip('::1::'))
        self.assertFalse(is_ip('1:'))
        self.assertFalse(is_ip(':1'))
        self.assertFalse(is_ip(':1:1:1::2'))
        self.assertFalse(is_ip('1:1:1:1:1:1:1:1:1:1:1:1:1:1:1:1'))
        self.assertFalse(is_ip('::11111'))
        self.assertFalse(is_ip('11111:1:1:1:1:1:1:1'))
        self.assertFalse(is_ip('2001:db8:0000:1:1:1:1::1'))
        self.assertFalse(is_ip('0:0:0:0:0:0:ffff:127.0.0.1'))
        self.assertFalse(is_ip('0:0:0:0:ffff:127.0.0.1'))
        print('OK - test_invalid_ip')

    def test_valid_ip_v4_num(self) -> bool:
        self.assertTrue(is_ip('127.0.0.1', 4))
        self.assertTrue(is_ip('0.0.0.0', 4))
        self.assertTrue(is_ip('255.255.255.255', 4))
        self.assertTrue(is_ip('1.2.3.4', 4))
        self.assertTrue(is_ip('255.0.0.1', 4))
        self.assertTrue(is_ip('0.0.1.1', 4))
        print('OK - test_valid_ip_v4_num')

    def test_invalid_ip_v4_num(self):
        self.assertFalse(is_ip('::1', 4))
        self.assertFalse(is_ip('2001:db8:0000:1:1:1:1:1', 4))
        self.assertFalse(is_ip('::ffff:127.0.0.1', 4))
        self.assertFalse(is_ip('137.132.10.01', 4))
        self.assertFalse(is_ip('0.256.0.256', 4))
        self.assertFalse(is_ip('255.256.255.256', 4))
        print('OK - test_invalid_ip_v4_num')

    def test_valid_ip_v4_str(self) -> bool:
        self.assertTrue(is_ip('127.0.0.1', "4"))
        self.assertTrue(is_ip('0.0.0.0', "4"))
        self.assertTrue(is_ip('255.255.255.255', "4"))
        self.assertTrue(is_ip('1.2.3.4', "4"))
        self.assertTrue(is_ip('255.0.0.1', "4"))
        self.assertTrue(is_ip('0.0.1.1', "4"))
        print('OK - test_valid_ip_v4_str')

    def test_invalid_ip_v4_str(self):
        self.assertFalse(is_ip('::1', "4"))
        self.assertFalse(is_ip('2001:db8:0000:1:1:1:1:1', "4"))
        self.assertFalse(is_ip('::ffff:127.0.0.1', "4"))
        self.assertFalse(is_ip('137.132.10.01', "4"))
        self.assertFalse(is_ip('0.256.0.256', "4"))
        self.assertFalse(is_ip('255.256.255.256', "4"))
        print('OK - test_invalid_ip_v4_str')

    def test_valid_ip_v6_num(self) -> bool:
        self.assertTrue(is_ip('::1', 6))
        self.assertTrue(is_ip('2001:db8:0000:1:1:1:1:1', 6))
        self.assertTrue(is_ip('::ffff:127.0.0.1', 6))
        self.assertTrue(is_ip('fe80::1234%1', 6))
        self.assertTrue(is_ip('ff08::9abc%10', 6))
        self.assertTrue(is_ip('ff08::9abc%interface10', 6))
        self.assertTrue(is_ip('ff02::5678%pvc1.3', 6))
        print('OK - test_valid_ip_v6_num')

    def test_invalid_ip_v6_num(self):
        self.assertFalse(is_ip('127.0.0.1', 6))
        self.assertFalse(is_ip('0.0.0.0', 6))
        self.assertFalse(is_ip('255.255.255.255', 6))
        self.assertFalse(is_ip('1.2.3.4', 6))
        self.assertFalse(is_ip('::ffff:287.0.0.1', 6))
        self.assertFalse(is_ip('%', 6))
        self.assertFalse(is_ip('fe80::1234%', 6))
        self.assertFalse(is_ip('fe80::1234%1%3%4', 6))
        self.assertFalse(is_ip('fe80%fe80%', 6))
        print('OK - test_invalid_ip_v6_num')

    def test_valid_ip_v6_str(self) -> bool:
        self.assertTrue(is_ip('::1', "6"))
        self.assertTrue(is_ip('2001:db8:0000:1:1:1:1:1', "6"))
        self.assertTrue(is_ip('::ffff:127.0.0.1', "6"))
        self.assertTrue(is_ip('fe80::1234%1', "6"))
        self.assertTrue(is_ip('ff08::9abc%10', "6"))
        self.assertTrue(is_ip('ff08::9abc%interface10', "6"))
        self.assertTrue(is_ip('ff02::5678%pvc1.3', "6"))
        print('OK - test_valid_ip_v6_str')

    def test_invalid_ip_v6_str(self):
        self.assertFalse(is_ip('127.0.0.1', "6"))
        self.assertFalse(is_ip('0.0.0.0', "6"))
        self.assertFalse(is_ip('255.255.255.255', "6"))
        self.assertFalse(is_ip('1.2.3.4', "6"))
        self.assertFalse(is_ip('::ffff:287.0.0.1', "6"))
        self.assertFalse(is_ip('%', "6"))
        self.assertFalse(is_ip('fe80::1234%', "6"))
        self.assertFalse(is_ip('fe80::1234%1%3%4', "6"))
        self.assertFalse(is_ip('fe80%fe80%', "6"))
        print('OK - test_invalid_ip_v6_str')
