'''
Things to manage projects in MagiCake
'''

import pygame as pg


class Project(pg.sprite.Sprite):
	'''
	This is object to represent information of a project
	'''

	def __init__(self, program, x, y, width, height, color):
		pg.sprite.Sprite.__init__(self)
		self.program = program
		
		# Visual representation
		self.image = pg.Surface((width, height))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y




		print("Project created")