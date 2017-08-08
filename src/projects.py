'''
Things to manage projects in MagiCake
'''

import pygame as pg

from settings import *


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



	def update(self):

		# Check for collision with mouse
		hits = pg.sprite.collide_rect(self, self.program.start_mouse)
		if hits:
			# Change background color on mouse over
			self.image.fill(BLUE)
		else:
			# In not mouse over
			self.image.fill(BLACK)

	def click(self):
		'''
		Instruction after clicking on object
		'''

		# Start project creator
		#start_new_project()
		pass


class ProjectCreator(pg.sprite.Sprite):
	'''
	This class creates projects
	'''
	def __init__(self):
		pass


def start_new_project():
	'''
	This function lounches project creator
	'''
	print("New project started")