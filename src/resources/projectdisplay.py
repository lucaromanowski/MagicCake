'''
Managing dysplaying of projects as a list with scroll bar
'''
import pygame as pg

from collections import deque
from settings import *



class ScrollListDisplay(pg.sprite.Sprite):
	'''
	This class takes group of sprites and returns a  list
	of projects to display with scroll bar
	'''

	def __init__(self,
				 program,
				 sprite_group, 
				 screen, 
				 x=WIDTH/2, 
				 y=HEIGHT/10-10,
				 width=500, 
				 height=HEIGHT - 80 , 
				 child_left_border=10,
				 child_right_border=10,
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
		self.sprite_group = self.set_initial_position(sprite_group, child_left_border,child_right_border, child_top_border)
		self.screen = screen



		print()
		print('ScrollListDIsplayCreated: ', str(self.sprite_group))
		print("RECT: ", str(self.rect))
	

	def set_initial_position(self,
							 collection, 
							 child_left_border,
							 child_right_border,
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
		print('seting up initial position for projects', "x: ",str(initial_x),"y: ", str(initial_y))
		
		# Sprite group wich will be returned
		self.positioned_sprites = pg.sprite.Group()
		# Reset positioned sprites group 
		if len(self.positioned_sprites) > 0:
			self.positioned_sprites.empty()

		# Position of last element
		last_pos = deque([initial_x, initial_y], 2)
		# Setting up initial position for collection elements
		for num, project in enumerate(collection):
			# Start counting form 1



			# Reset project position
			project.rect.y = initial_y
			print(str(num)," | ", str(project))
			# Change position of current rect
			# In case of first project we just set x, and y position to initial_x and initial_y values
			if num == 0:
				project.rect.y = initial_y
				project.rect.x = initial_x
				# Add project sprite to the group
				self.positioned_sprites.add(project)

			else:
				project.rect.x = initial_x
				project.rect.y = last_pos[1] + project.rect.height + spacing
				# Keep last x position
				last_pos.append(project.rect.x)
				# Keep last y position
				last_pos.append(project.rect.y)
				# Add project sprite to the group
				self.positioned_sprites.add(project)


			print("last pos: ", str(last_pos))


		return self.positioned_sprites


	def update(self):
		'''
		This method checks if colelction elements are within boundaries of Scroll Display 
		and updates the list of projects to display
		'''

		# Create group of objects to display
		self.collection_to_display = pg.sprite.Group()
		self.collection_to_display.empty()

		# Check wich objects are within the boundaries of display box
		for project in self.sprite_group:
			if self.rect.bottom > project.rect.bottom > self.rect.y:
				self.collection_to_display.add(project) 


	def get_projects_to_display(self):
		'''
		This method returnd projects to display
		'''
		return self.collection_to_display


	def draw_border(self, surface, color, width=40):
		'''
		This method draws boarder around to cover elements of collection
		'''

		# Setting top positions
		start_pos_top = (self.rect.x, self.rect.y- 20)
		end_pos_top = (self.rect.x + self.rect.width, self.rect.y- 20)
		# Setting buttom positions
		start_pos_bottom = (self.rect.x, self.rect.y + self.rect.height+20)
		end_pos_bottom = (self.rect.x + self.rect.width, self.rect.y+self.rect.height+20)

		# Draw top line
		pg.draw.line(surface, color, start_pos_top, end_pos_top, width)
		# Draw bottom line
		pg.draw.line(surface, color, start_pos_bottom, end_pos_bottom, width+20)


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
		self.attached_to = attached_to

		# Setting up collection wich will be controlled by side bar
		self.collection = collection

		# Scroll bar positioning
		self.procent_position = 1
		self.min_position_y = 50
		self.max_position_y = 510
		self.min_abs_position_y = 1
		self.max_abs_position_y = self.max_position_y - self.min_position_y
		self.max_collection_y = [i.rect.y for i in self.collection][-1]
		self.factor = int(self.max_collection_y/self.max_position_y) 
		print('max position y: ', str(self.max_position_y))
		print('max abs position y: ', str(self.max_abs_position_y))
		print('max collection y: ', str(self.max_collection_y))
		print('factor: ', str(self.factor))
		
		# Checking if there is any object the SideBar is attached to.
		# If it exists, SideBar is positioned relativly to this object.
		if attached_to:
			self.rect.x = attached_to.rect.x + attached_to.rect.width + spacing
			self.rect.y = attached_to.rect.y
		else:
			self.rect.x = x
			self.rect.y = y

		print('Side bar position x: ', str(self.rect.x), ' | position y: ', str(self.rect.y))

		# Flags
		self.is_hover = False
		self.is_scrollable = False # This flag helps to move side bar when coursor is of the side bar

		# Getting old position (in this case initial position)
		self.old_pos = self.rect.y
		self.change_pos = 0
		

		print()
		print("Side bar collection: ", str(self.collection))
		print()
		print('Side bar created')


	def update(self):
		'''
		This method updates position of all elements in collection.
		'''

		# Side bar move
		# Checking if any mouse button is pressed
		mp = pg.mouse.get_pressed()
		# Getting mouse position
		pos = pg.mouse.get_pos()
		# Checking for collision between mouse and side bar
		if mp[0]:
			if (self.rect.x + self.rect.width) > pos[0] > self.rect.x and (self.rect.y + self.rect.height) > pos[1] > self.rect.y:
				# if collision occurs set flag o true
				self.is_scrollable = True
			if self.is_scrollable:
				# if flag is set to true, change side bar position accordingly to mouse position
				self.rect.y = pos[1]
		# if mouse button 1 is not pressed, disable scrolling
		else:
			self.is_scrollable = False

		# Get change of scroll bar position
		if self.old_pos != self.rect.y:
			self.change_pos = self.rect.y - self.old_pos
		else:
			self.new_pos = self.old_pos
			self.change_pos = 0

		print()
		print('Old position: ', str(self.old_pos))
		print('New position: ', str(self.new_pos))
		print('Change position: ', str(self.change_pos))
		print()
		
		# Change position of collection elementacordingly to change and factor
		if self.change_pos != 0:
			for project in self.collection:
				project.rect.y -= self.change_pos * self.factor
				print()
				print("Pozycja y projectu w kolekcji: ", str(project.rect.y))





		

		# Set boundaries relative to attached element position
		# Top boundary
		if self.rect.y < self.attached_to.rect.y:
			self.rect.y = self.attached_to.rect.y
		# Bottom boundary
		if self.rect.bottom > self.attached_to.rect.height:
			self.rect.bottom = self.attached_to.rect.height + self.attached_to.rect.y

		#print()
		#print("Sidebar y position: ", str(self.rect.y))


		# Getting old position
		self.old_pos = self.rect.y


			
				


