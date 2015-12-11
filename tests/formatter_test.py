from t3.formatter import PlainFormatter
import unittest
import os

class Formatter_Test(unittest.TestCase):
	
	def test_basic_formatting_itself(self):
		formatter = PlainFormatter("../code_snippets/python/csv_snip.py")
		length = len(formatter.format())
		self.assertEqual(length,1382) # if it reaches here then there was no issue		
		
		
		
	def test_error_thrown_when_wrong_file_given(self):
		pass
		


if __name__=="__main__":
	unittest.main()	
