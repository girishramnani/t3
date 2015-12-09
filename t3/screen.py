import curses

class JsonDict(dict):
	def __getattr__(self,value):
		if value in self:
			return self[value]
		else:
			super().__getattr__(value)
	
	
		

class Screen(object):
	def __init__(self,buffer):
		self.buffer = buffer
		

	
	def __call__(self,stdscr):
		"""working along the wrapper of the curses for better opening an closing of the program"""
		self.window = stdscr
	
	
	

class WrappingPoint(object):

	def __init__(self,size,x=0,y=0):
		self._x = x
		self._y = y
		self.size=JsonDict(x=size[1],y=size[0])
		self.old =JsonDict(x=-1,y=-1)
			
		
		
	@property
	def x(self):
		return self._x
	@property
	def y(self):
		return self._y
	
	@x.setter	
	def x(self,value):
		self.old.x = self._x
		self._x = value%self.size.x
	
	@y.setter
	def y(self,value):
		self.old.y = self._y
		self._y = value%self.size.y
	
	

class Buffer(object):
	
	"""
	This object is responsible for the cursor movement and coloring of the code
	
	"""	
	
	def __init__(self,init_loc):
		self.init_loc = init_loc
				
		

