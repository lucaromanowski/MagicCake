'''
Managing dysplaying of projects as a list with scroll bar
'''

class ScrollListDisplay(object):
	'''
	This class takes group of sprites and display them on the screen as a list 
	of projects with scroll bar
	'''

	def __init__(self, program, sprite_group, screen):
		self.program = program
		self.sprite_group = sprite_group
		self.screen = screen

		print()
		print('ScrollListDIsplayCreated: ', str(self.sprite_group))
	

	def set_initial_position(self, collection):
		'''
		This method sets position for all sprites in collection
		Sprites stack one under another
		'''
		pass