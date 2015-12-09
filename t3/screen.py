import curses


class Screen(object):
	def __init__(self,buffer):
		self.buffer = buffer
		

	
	def __call__(self,stdscr):
		"""working along the wrapper of the curses for better opening an closing of the program"""
		self.window = stdscr
	
	
	

class Location(object):

	def __init__(self,size,x=0,y=0):
		self._x = x
		self._y = y
		self.size=size
	
	@property
	def x(self):
		return self._x%self.size[1]
	
	@property
	def y(self):
		return self._y%self.size[0]	
	
	@x.setter	
	def x(self,value):
		self._x = value%self.size[1]
	
	@y.setter
	def y(self,value):
		self._y = value%self.size[0]
	

class Buffer(object):
	
	"""
	This object is responsible for the cursor movement and coloring of the code
	
	"""	
	
	def __init__(self,init_loc):
		self.init_loc = init_loc
				
		

