import unittest
from t3.screen import WrappingPoint

class Location_test(unittest.TestCase):
	
	
	def setUp(self):
		self.loc = WrappingPoint((20,20))
		
	
	def test_for_simple(self):
		self.assertEqual(self.loc.x,0)
		self.assertEqual(self.loc.y,0)
	
	def test_for_adding(self):
		self.loc.x+=21
		self.assertEqual(self.loc.x,1)
		
	def test_for_subtraction(self):
		self.loc.y-=1
		self.assertEqual(self.loc.y,19)
		
	
if __name__ =="__main__":
	unittest.main()
