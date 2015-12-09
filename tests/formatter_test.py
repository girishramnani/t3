from t3.formatter import Formatter
import unittest

class Formatter_Test(unittest.TestCase):
	
	def test_basic_formatting_itself(self):
		formatter = Formatter("formatter_test.py")
		formatter.format()
		self.assertEqual(True,True) # if it reaches here then there was no issue		
		
		
		
	def test_error_thrown_when_wrong_file_given(self):
		pass
		


if __name__="__main__":
	unittest.main()	
