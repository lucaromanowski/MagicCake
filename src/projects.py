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




		#print("Project created, name: ", str(self.name))



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

		#print("Project creator lunched")







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
		
		#print("New project started")
		
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
				pass


			

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
		self.name = "project_create_button"
		self.is_creatable = False


	def update(self):
		# Check for collision with mouse
		hits = pg.sprite.collide_rect(self, self.program.creator_mouse)
		# In case user didn't type anything as project name, display button as black and white
		if len(self.program.input.input_list) == 0:
			if hits:
				self.image.fill(LIGHT_GREY)
			else:
				self.image.fill(DARK_GREY)
		else:
			# Case when user typed anything as project name
			if hits:
				# In case user didn't type anything as project name, display button as black and white
				if len(self.program.input.input_list) == 0:
					self.image.fill(LIGHT_GREY)
				else:
					# Change background color on mouse over
					self.image.fill(PINKY)
					self.is_highlighted = True
			else:
				# In not mouse over
				self.image.fill(LILA)
				self.is_highlighted = False


	def draw_text(self, surface):
		'''
		This method displays text on the button
		'''
		
		# Drawing cakes name
		# Drawing text inside of self surface
		# Select the font to use, size, bold, italics
		font = pg.font.SysFont('Courier', 22, False, False)
		 
		# Render the text. "True" means anti-aliased text.
		# Black is the color. The variable BLACK was defined
		# above as a list of [0, 0, 0]
		# Note: This line creates an image of the letters,
		# but does not put it on the screen yet.
		text = font.render("Create", True, WHITE)
		 
		# Put the image of the text on the screen at 250x250
		surface.blit(text, [self.rect.x + 60, self.rect.y + 13])




def check_for_creator_events(starter):
	
	
	# Check for quit event
	for event in pg.event.get():
			if event.type == pg.QUIT:
				starter.looping = False

def check_for_keyboard_input(magiccake):


	for event in pg.event.get():
			if event.type == pg.QUIT:
				magiccake.screen_number = 0
				magiccake.start_running = False
				magiccake.creator_running = False
				magiccake.control_loop = False
				
			
				
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
				# if event.key == pg.K_RETURN  :
				# 	# Check if there is a name for project
				# 	if len(magiccake.input.input_list) > 0:
						
				# 		# Check if we are in project creating mode
				# 		if magiccake.is_creating:
							
				# 			# Create project
				# 			p = Project(magiccake, 0, 0, 200, 40, BLACK, magiccake.input.input_str )

				# 			# Clear current project (only one current project may be in a group)
				# 			try:
				# 				magiccake.current_project.empty()
				# 				print('Current project group cleared')
				# 			except:
				# 				pass
				# 			# Setting up new project as current project in our program
				# 			magiccake.current_project.add(p)
				# 			print('current project set up')



				# 			# Clear input
				# 			magiccake.input.clear()

				# 			# Exit creator
				# 			magiccake.creator_running = False

							
			
			# Check for mouse clicking
			if event.type == pg.MOUSEBUTTONUP:
				
				hits = pg.sprite.spritecollide(magiccake.creator_mouse, magiccake.all_creator_sprites, False)
				
				if hits:
					# Check if we clicked create button
					if hits[0].name == "project_create_button":
						# Allow to create new project if user typed anything
						if len(magiccake.input.input_list) > 0:

							# Create project and set it as current project
							# Check if there is no project with name that user typed
							exists = project_already_exists(magiccake.input.input_str, magiccake.project_loader.all_loaded_projects)
							# Case when project alreaddy exists
							if exists:
								# Give a message that user need to change project name
								print('This name already exists')
							else:
								# Create new project
								magiccake.current_project = magiccake.project_creator.create_project(str(magiccake.input.input_str))

								# Clear input
								magiccake.input.clear()

								# Set screen to main
								magiccake.screen_number = 2

								# Exit create screen
								magiccake.creator_running = False
					
				

def project_already_exists(name, projects):
	'''
	This function chcecks if the project name of new project already exists..
	'''
	exists = False
	# If exists
	for project in projects:
		# Check if given name is equel to at least one name of already existing projects 
		if project.name == name:
			exists = True
			# There is no need to check more
			#print("Project name match")
			break
	# Return True or False		
	return exists