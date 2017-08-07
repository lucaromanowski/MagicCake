import pygame as pg

from projects import *
from settings import *


def start_text(x, y, surface, text, size, font_name='Calibri', is_Bold=True, is_Italic=False, is_Aa=True, color=BLACK):
	'''
	Function used in start menu to draw text
	'''
	font = pg.font.SysFont(font_name, size, is_Bold, is_Italic)	 
	text_to_display = font.render(text, is_Aa, color)	
	surface.blit(text_to_display, [x, y])



class Start(pg.sprite.Sprite):
	'''
	Start button
	'''

	def __init__(self, program, x, y, text):
		pg.sprite.Sprite.__init__(self)
		self.program = program
		self.image = pg.Surface((260, 40))
		self.image.fill(PINKY)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		# Status
		self.is_highlighted = False

		self.text = text

	def update(self):
		
		# Check for collision with mouse
		hits = pg.sprite.collide_rect(self, self.program.start_mouse)
		if hits:
			# Change background color on mouse over
			self.image.fill(BLUE)
			self.is_highlighted = True
			
		else:
			# In not mouse over
			self.image.fill(BLACK)
			self.is_highlighted = False

	def draw_text(self, surface):
		
		# Drawing cakes name
		# Drawing text inside of self surface
		# Select the font to use, size, bold, italics
		font = pg.font.SysFont('Courier', 18, False, False)
		 
		# Render the text. "True" means anti-aliased text.
		# Black is the color. The variable BLACK was defined
		# above as a list of [0, 0, 0]
		# Note: This line creates an image of the letters,
		# but does not put it on the screen yet.
		text = font.render(self.text, True, PINKY)
		 
		# Put the image of the text on the screen at 250x250
		surface.blit(text, [self.rect.x + 3, self.rect.y + 10])
			



class Create(pg.sprite.Sprite):
	'''
	Create button
	'''

	def __init__(self, program, x, y, text):
		pg.sprite.Sprite.__init__(self)
		self.program = program
		self.image = pg.Surface((260, 40))
		self.image.fill(PINKY)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		# Status
		self.is_highlighted = False

		self.text = text



	def update(self):
		
		# Check for collision with mouse
		hits = pg.sprite.collide_rect(self, self.program.start_mouse)
		if hits:
			# Change background color on mouse over
			self.image.fill(BLUE)
			self.is_highlighted = True

		else:
			# In not mouse over
			self.image.fill(BLACK)
			self.is_highlighted = False
			



	def draw_text(self, surface):
		
		# Drawing cakes name
		# Drawing text inside of self surface
		# Select the font to use, size, bold, italics
		font = pg.font.SysFont('Courier', 18, False, False)
		 
		# Render the text. "True" means anti-aliased text.
		# Black is the color. The variable BLACK was defined
		# above as a list of [0, 0, 0]
		# Note: This line creates an image of the letters,
		# but does not put it on the screen yet.
		text = font.render(self.text, True, PINKY)
		 
		# Put the image of the text on the screen at 250x250
		surface.blit(text, [self.rect.x + 3, self.rect.y + 10])


	def create_new_project(self):
		"""
		This method creates Project Creator
		"""
		pass

