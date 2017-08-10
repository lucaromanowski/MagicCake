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

	def __init__(self, program, x, y, width, height, color, name):
		pg.sprite.Sprite.__init__(self)
		self.program = program
		
		# Visual representation
		self.image = pg.Surface((width, height))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.name = name




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
	Basic class that handels project creator loop
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
			try:
				self.creator_mouse_group.draw(self.program.screen)
			except:
				print('drw exception')


			

			# update whole screen
			pg.display.update()



class CreateProjectButton(pg.sprite.Sprite):
	'''
	Button that creats new project
	'''

	def __init__(self, program):
		pg.sprite.Sprite.__init__(self)
		self.program = program

		# Visual representation
		self.image = pg.Surface((200, 50))
		self.image.fill(LILA)
		self.rect = self.image.get_rect()
		self.rect.x = WIDTH - self.rect.width - 20
		self.rect.y = HEIGHT - self.rect.height - 20

	def update(self):

		# Check for collision with mouse
		hits = pg.sprite.collide_rect(self, self.program.creator_mouse)
		if hits:
			# Change background color on mouse over
			self.image.fill(PINKY)
			self.is_highlighted = True

		else:
			# In not mouse over
			self.image.fill(LILA)
			self.is_highlighted = False




def check_for_creator_events(starter):
	
	
	# Check for quit event
	for event in pg.event.get():
			if event.type == pg.QUIT:
				starter.looping = False

def check_for_keyboard_input(magiccake):


	for event in pg.event.get():
			if event.type == pg.QUIT:
				magiccake.creator_running= False
			
				
			# Check for keyboard for typing letters
			if event.type == pg.KEYDOWN:
				# Checking if the name is not to long
				if not len(magiccake.input.input_list) > 35:
					# Checking if youa are on a main page
					
					if event.key == pg.K_a:
						magiccake.input.input_list.append('a')
					if event.key == pg.K_b:
						magiccake.input.input_list.append('b')
					if event.key == pg.K_c:
						magiccake.input.input_list.append('c')
					if event.key == pg.K_d:
						magiccake.input.input_list.append('d')
					if event.key == pg.K_e:
						magiccake.input.input_list.append('e')
					if event.key == pg.K_f:
						magiccake.input.input_list.append('f')
					if event.key == pg.K_g:
						magiccake.input.input_list.append('g')
					if event.key == pg.K_h:
						magiccake.input.input_list.append('h')
					if event.key == pg.K_i:
						magiccake.input.input_list.append('i')
					if event.key == pg.K_j:
						magiccake.input.input_list.append('j')
					if event.key == pg.K_k:
						magiccake.input.input_list.append('k')
					if event.key == pg.K_l:
						magiccake.input.input_list.append('l')
					if event.key == pg.K_m:
						magiccake.input.input_list.append('m')
					if event.key == pg.K_n:
						magiccake.input.input_list.append('n')					
					if event.key == pg.K_o:
						magiccake.input.input_list.append('o')
					if event.key == pg.K_p:
						magiccake.input.input_list.append('p')
					if event.key == pg.K_r:
						magiccake.input.input_list.append('r')
					if event.key == pg.K_s:
						magiccake.input.input_list.append('s')
					if event.key == pg.K_t:
						magiccake.input.input_list.append('t')
					if event.key == pg.K_u:
						magiccake.input.input_list.append('u')
					if event.key == pg.K_w:
						magiccake.input.input_list.append('w')
					if event.key == pg.K_x:
						magiccake.input.input_list.append('x')
					if event.key == pg.K_y:
						magiccake.input.input_list.append('y')
					if event.key == pg.K_z:
						magiccake.input.input_list.append('z')
					if event.key == pg.K_SPACE:
						magiccake.input.input_list.append(' ')
					if event.key == pg.K_PERIOD:
						magiccake.input.input_list.append('.')

					# Checking for cyfer input
					if event.key == pg.K_0:
						magiccake.input.input_list.append('0')
					if event.key == pg.K_1:
						magiccake.input.input_list.append('1')
					if event.key == pg.K_2:
						magiccake.input.input_list.append('2')
					if event.key == pg.K_3:
						magiccake.input.input_list.append('3')
					if event.key == pg.K_4:
						magiccake.input.input_list.append('4')
					if event.key == pg.K_5:
						magiccake.input.input_list.append('5')
					if event.key == pg.K_6:
						magiccake.input.input_list.append('6')
					if event.key == pg.K_7:
						magiccake.input.input_list.append('7')
					if event.key == pg.K_8:
						magiccake.input.input_list.append('8')
					if event.key == pg.K_9:
						magiccake.input.input_list.append('9')
				
				if event.key == pg.K_BACKSPACE:
					if len(magiccake.input.input_list) > 0:
						magiccake.input.input_list.pop() 

				# Making cake after user presses enter key
				if event.key == pg.K_RETURN  :
					# Check for page 1
					if magiccake.current_page == 1:
						if len(magiccake.input.input_list) > 0:
							for cake in magiccake.all_cakes:
								if cake.is_active:
									# Create ingredient and add it to cake
									i = Ingredient(magiccake, magiccake.input.input_str, WIDTH + 20, 20 + 40 * len(cake.ingredients))
									cake.ingredients.add(i)
									#print('INGREDIENT CREATED named: ' + str(i.name))
									magiccake.input.input_list = []
									break
							if len(magiccake.input.input_list) > 0:
								# Create cake and add it to groups
								cake = Cake(magiccake, magiccake.input.input_str)
								#magiccake.all_sprites.add(cake)
								magiccake.all_cakes.add(cake)
								# Clear input
								magiccake.input.input_list = []
							




			
			# Check for mouse clicking
			if event.type == pg.MOUSEBUTTONUP:
				
				# Checks for klicking on Paginator objects
				pass


				

				
							
				

