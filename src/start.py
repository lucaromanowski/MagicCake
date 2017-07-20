import pygame as pg

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

	def __init__(self, program, x, y):
		pg.sprite.Sprite.__init__(self)
		self.program = program
		self.image = pg.Surface((160, 40))
		self.image.fill(PINKY)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self):
		pass
