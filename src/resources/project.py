'''
Project class 
'''

import pygame as pg

from settings import *


class NewProject(pg.sprite.Sprite):
	'''
	Class that holds reference to all cakes in project.

	'''

	def __init__(self, name, width=300, height=40, x=WIDTH*3/4, y=HEIGHT/3):
		pg.sprite.Sprite.__init__(self)
		self.name = name
		self.cakes = []

		# Visual representation
		self.image = pg.Surface((width, height))
		self.image.fill(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		print('Visual project created')

