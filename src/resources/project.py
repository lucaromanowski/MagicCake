'''
Project class 
'''

import pygame as pg

from settings import *


class NewProject(pg.sprite.Sprite):
	'''
	Class that holds reference to all cakes in project.

	'''

	def __init__(self, name, width=480, height=40, x=WIDTH*3/4, y=HEIGHT/3):
		pg.sprite.Sprite.__init__(self)
		self.name = name
		self.cakes = []

		# Visual representation
		self.image = pg.Surface((width, height))
		self.image.fill(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.is_hover = False
		#self.is_selected = False


	def display_text(self, surface):
		'''
		This method displays info about project
		'''
		myfont = pg.font.SysFont('Tahoma', 14)
		textsurface = myfont.render(str(self.name), False, WHITE)
		surface.blit(textsurface,(self.rect.x+10,self.rect.y+11))


	def update(self):
		# Check for collisions with mouse
		mp = pg.mouse.get_pos()
		if self.rect.x + self.rect.width > mp[0] > self.rect.x and self.rect.y + self.rect.height > mp[1] > self.rect.y:
			self.image.fill(RED)
			self.is_hover = True
		else:
			self.image.fill(BLACK)
			self.is_hover = False
			print('project is hover')

		# Change background collor of selected element
		#if self.is_selected:
			#self.image.fill(RED)
			#print('Project is selected')
		#else:
			#self.image.fill(BLACK)

