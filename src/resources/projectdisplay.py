'''
Managing dysplaying of projects as a list with scroll bar
'''
import pygame as pg

from settings import *


class ScrollListDisplay(pg.sprite.Sprite):
	'''
	This class takes group of sprites and display them on the screen as a list 
	of projects with scroll bar
	'''

	def __init__(self,
				 program,
				 sprite_group, 
				 screen, 
				 x=WIDTH/2, 
				 y=HEIGHT/10-10,
				 width=500, 
				 height=400, 
				 child_left_border=10,
				 child_top_border=10):

		pg.sprite.Sprite.__init__(self)
		# Visual reprezentation
		self.image = pg.Surface((width, height))
		self.image.fill(PINK)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		# Data 
		self.program = program
		self.sprite_group = self.set_initial_position(sprite_group, child_left_border, child_top_border)
		self.screen = screen



		print()
		print('ScrollListDIsplayCreated: ', str(self.sprite_group))
		print("RECT: ", str(self.rect))
	

	def set_initial_position(self,
							 collection, 
							 child_left_border,
							 child_top_border,
							 initial_x=None, 
							 initial_y=None, 
							 spacing=10):
		'''
		This method sets initial position for all sprites in collection
		Sprites stack one under another
		'''

		# Setting up initial values for x and y using rect of Scroller
		if initial_x == None:
			initial_x = self.rect.x + child_left_border
		if initial_y == None:
			initial_y = self.rect.y + child_top_border


		print()
		print('seting up initial position for projects')


		return collection


	#def update(self, scroll_bar):
		'''
		This method updates position of all collection elements accordingly with position
		of side scroll bar.
		'''
		#pass


class SideBar(pg.sprite.Sprite):
	'''
	This class represents side bar. 
	'''
	def __init__(self, program, width, height, x=30, y=60, collection=None, attached_to=None, spacing=10):
		pg.sprite.Sprite.__init__(self)
		self.program = program
		self.image = pg.Surface((width, height))
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		
		# Checking if there is any object the SideBar is attached to.
		# If it exists, SideBar is positioned relativly to this object.
		if attached_to:
			self.rect.x = attached_to.rect.x + attached_to.rect.width + spacing
			self.rect.y = attached_to.rect.y
		else:
			self.rect.x = x
			self.rect.y = y

		print('Side bar position x: ', str(self.rect.x), ' | position y: ', str(self.rect.y))

		self.is_hover = False

		# Setting up collection wich will be controlled by side bar
		self.collection = collection


		print()
		print('Side bar created')


	def update(self):
		'''
		This method updates position of all elements in collection.
		'''

		pass
