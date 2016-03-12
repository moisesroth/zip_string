import unittest
from zip_string import zip_string

class TestZip_StringFunction(unittest.TestCase):

    def test_0(self):
      self.assertEqual(zip_string('a'), 'a')

    def test_1(self):
      self.assertEqual(zip_string('abcd'), 'a-d')

    def test_2(self):
      self.assertEqual(zip_string('hijlbcd'), 'h-jlb-d')

    def test_3(self):
      self.assertEqual(zip_string('ihdlkioabcihgfe'), 'ihdlkioa-ci-e')

    def test_4(self):
      self.assertEqual(zip_string('cba'), 'c-a')

    def test_5(self):
      self.assertEqual(zip_string('zyx'), 'z-x')

    def test_6(self):
      self.assertEqual(zip_string('abcdcba'), 'a-d-a')

    def test_7(self):
      self.assertEqual(zip_string('abcddcba'), 'a-dd-a')

    def test_8(self):
      self.assertEqual(zip_string('abcba'), 'a-c-a')

    def test_9(self):
      self.assertEqual(zip_string('abcbabcdefgfec'), 'a-c-a-g-ec')
      
if __name__ == '__main__':
    unittest.main()
