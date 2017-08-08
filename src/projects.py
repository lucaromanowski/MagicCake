'''
Things to manage projects in MagiCake
'''

import pygame as pg

from settings import *
from sprites import *


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
	def __init__(self, program):
		pg.sprite.Sprite.__init__(self)
		self.program = program

		# Visual representation
		self.image = pg.Surface((500, 500))
		self.image.fill(LILA)
		self.rect = self.image.get_rect()
		self.rect.x = WIDTH/2 - self.rect.width/2
		self.rect.y = HEIGHT/2 - self.rect.height/2

		print("Project creator lunched")







class ProjectStarter(object):
	'''
	Basic class that handels loop
	'''
	def __init__(self, program):
		self.program = program


	def start_new_project(self):
		'''
		This method lounches project creator
		'''
		
		print("New project started")
		
		self.pc = ProjectCreator(self.program)
		self.creator_mouse = Mouse(self.program)

		# Creator groups
		self.creator_mouse_group = pg.sprite.Group()

		# Adding to groups
		self.creator_mouse_group.add(self.creator_mouse)
		
		# main loop starts
		self.loop()
	
	def loop(self):
		self.looping = True
		while self.looping:
			self.program.clock.tick(FPS)
			# ----------EVENTS---------

			

			check_for_creator_events(self)

			# ---------UPDATE
			# Moude update
			self.creator_mouse_group.update()
			self.mouse_pos = pg.mouse.get_pos()
			print(self.mouse_pos)
			

			#

			# ---------DRAW

			# Filling with color OBLIGATORY
			self.program.screen.fill(MENU_BACKGROUND_COLOR)

			# Mouse draw
			self.creator_mouse_group.draw(self.program.screen)


			

			# update whole screen
			pg.display.update()



def check_for_creator_events(starter):
	
	
	# Check for quit event
	for event in pg.event.get():
			if event.type == pg.QUIT:
				starter.looping = False