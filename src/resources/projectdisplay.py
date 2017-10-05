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

		self.selected_project = deque([], 1)



		#print()
		#print('ScrollListDIsplayCreated: ', str(self.sprite_group))
		#print("RECT: ", str(self.rect))
	

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


		#print()
		#print('seting up initial position for projects', "x: ",str(initial_x),"y: ", str(initial_y))
		
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
			#print(str(num)," | ", str(project))
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


			#print("last pos: ", str(last_pos))


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
		start_pos_bottom = (self.rect.x, self.rect.y + self.rect.height+30)
		end_pos_bottom = (self.rect.x + self.rect.width, self.rect.y+self.rect.height+30)

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
		self.max_collection_y = [i.rect.y for i in self.collection][-1] #This is used only to calculate factor
		self.factor = int(self.max_collection_y/self.max_position_y) 
		#print('max position y: ', str(self.max_position_y))
		#print('max abs position y: ', str(self.max_abs_position_y))
		#print('max collection y: ', str(self.max_collection_y))
		#print('factor: ', str(self.factor))

		# Collection max and min position
		self.collection_max_y_position = self.min_position_y + 5
		self.collection_min_y_position = [i.rect.y for i in self.collection][-1] * - 1
		
		# Checking if there is any object the SideBar is attached to.
		# If it exists, SideBar is positioned relativly to this object.
		if attached_to:
			self.rect.x = attached_to.rect.x + attached_to.rect.width + spacing
			self.rect.y = attached_to.rect.y
		else:
			self.rect.x = x
			self.rect.y = y

		#print('Side bar position x: ', str(self.rect.x), ' | position y: ', str(self.rect.y))

		# Flags
		self.is_hover = False
		self.is_scrollable = False # This flag helps to move side bar when coursor is of the side bar

		# Getting old position (in this case initial position)
		self.old_pos = self.rect.y
		self.change_pos = 0
		

		#print()
		#print("Side bar collection: ", str(self.collection))
		#print()
		#print('Side bar created')


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


		# Getting mouse position
		#mp = pg.mouse.get_pos()

		# Checking if mouse position is within an interval of side bar min and max positions
		if self.max_position_y > pos[1] > self.min_position_y:
			# Get change of scroll bar position
			if self.old_pos != self.rect.y:
				self.change_pos = self.rect.y - self.old_pos
			else:
				self.new_pos = self.old_pos
				self.change_pos = 0
		else:
			# When mouse is not within side bar max and mine position interval, do not allow to change projects positions
			self.new_pos = self.old_pos
			self.change_pos = 0


		#print()
		#print('Old position: ', str(self.old_pos))
		#print('New position: ', str(self.new_pos))
		#print('Change position: ', str(self.change_pos))
		#print()
		#print("Collection max poss y: ", str(self.collection_max_y_position))
		#print("Collection min poss y: ", str(self.collection_min_y_position))



		# Make collection a list instead of pygame sprite group
		non_sprite_group_collction = [project for project in self.collection]


		# By how many % scroll bar position change?
		proc_change = int(self.change_pos/460 * 100)
		#print()
		#print("Side bar changed by: ", str(proc_change), " %")

		# Set position of sprites



		# Set first sprite to max and min position if necessery
		# Check if position of first sprite is greater than Ymax
		if non_sprite_group_collction[0].rect.y > self.collection_max_y_position:
			# Set first sprite y position to max position
			non_sprite_group_collction[0].rect.y = self.collection_max_y_position
		
		# Check if position of first sprite is smaller than  Ymin
		elif non_sprite_group_collction[0].rect.y < self.collection_min_y_position:
			# Set  first sprite y position to min position
			non_sprite_group_collction[0].rect.y = self.collection_min_y_position

		# Change position of first sprite acordlingly to side bar change
		# Check if scroll bar moved up
		if self.change_pos < 0:
			# Change position of first element in sprite group
			non_sprite_group_collction[0].rect.y -= proc_change/100 * sum(sprite.rect.height for sprite in non_sprite_group_collction) 
		# Check if scroll bar moved down
		elif self.change_pos > 0:
			# Change position of first element in sprite group
			non_sprite_group_collction[0].rect.y -= proc_change/100 * sum(sprite.rect.height for sprite in non_sprite_group_collction) 


		#print()
		#print("Position y of first element: ", str(non_sprite_group_collction[0].rect.y))



		# Position all elements in collection accordingly to first element
		for num, project in enumerate(non_sprite_group_collction):
			# Do nothing to first element
			if num == 0:
				continue
			else:
				# Position element below precedent element + spaceing
				non_sprite_group_collction[num].rect.y = non_sprite_group_collction[num-1].rect.y + non_sprite_group_collction[num].rect.height + 5 

		
		# Safety --> if sidebar reaches its min or max position, position first element of collection in max or min position
		if self.rect.y == self.min_position_y:
			non_sprite_group_collction[0] = self.collection_max_y_position
		elif self.rect.y == self.max_position_y:
			non_sprite_group_collction[0] = self.collection_min_y_position

		
		# Set boundaries relative to attached element position
		# Top boundary
		if self.rect.y < self.attached_to.rect.y:
			self.rect.y = self.attached_to.rect.y
		# Bottom boundary
		if self.rect.bottom > self.attached_to.rect.height:
			self.rect.bottom = self.attached_to.rect.height + self.attached_to.rect.y

		# Getting old position
		self.old_pos = self.rect.y


			
				


