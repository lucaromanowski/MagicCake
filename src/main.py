import pygame as pg

from projects import *
from remember import *
from settings import *
from sprites import *
from utils import *
from start import *

from resources.test import testfunc
from resources.listofprojects import ListOfProjects
from resources.project import NewProject
from resources.projectcreator import ProjectCreator
from resources.projectdisplay import ScrollListDisplay, SideBar
from resources.projectloader import ProjectLoader
from resources.projectsaver import ProjectSaver


class MagicCake:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		self.clock = pg.time.Clock()
		# Inital mouse  position
		self.mouse_pos = pg.mouse.get_pos()

		# Pagination pages
		self.current_page = 1

		# Set to true when create project screen is on
		self.is_creating = False

		# Projects management
		#self.current_project = 'Test cureeent project should be set to None'


	def new(self):
		# Create groups
		self.all_sprites = pg.sprite.Group() # Except: Cake
		self.all_cakes = pg.sprite.Group()
		self.paginators = pg.sprite.Group()
		self.scrollers = pg.sprite.Group()
		self.arrows = pg.sprite.Group()

		# Create objects
		self.input = Input(self)
		self.all_sprites.add(self.input)
		self.cakegeneral = CakeGeneral(self)
		self.all_sprites.add(self.cakegeneral)
		self.trash = Trash(self)
		self.all_sprites.add(self.trash)
		#self.cakedetail = CakeDetail(self)
		#self.all_sprites.add(self.cakedetail)

		# Paginator
		self.paginator_right = Paginator(self, 40, 'right')
		self.paginator_left = Paginator(self, - 40, 'left')
		self.all_sprites.add(self.paginator_left)
		self.paginators.add(self.paginator_left)
		self.all_sprites.add(self.paginator_right)
		self.paginators.add(self.paginator_right)

		# Scrollers
		self.scroller = Scroller(self)
		self.scrollers.add(self.scroller)
		# Arrows
		self.arrow_left = Arrow(self, 'left', WIDTH/2 - 150, HEIGHT/3 + 70)
		self.arrow_right = Arrow(self, 'right', WIDTH/2 - 80, HEIGHT/3 + 70)
		self.arrows.add(self.arrow_left)
		self.arrows.add(self.arrow_right)

		# Mouse coursor(invislibe or red)
		self.mouse = Mouse(self)
		self.all_sprites.add(self.mouse)

		# List object for displaying collections (Cakes, Ingredients)
		self.list = List(self)
		
		# Ingredients list
		self.ingredients_collection = List(self)

		# Current project
		self.current_project = None		


		# # Screen selector
		self.screen_number = 0
		self.screens = ['start_screen', 'create_screen', 'main_screen']
		self.current_screen = self.screens[self.screen_number]

		





		#--------------------------------TEST--------------------------------------------------------------------
		### Create cake with ingredient with protein
		#self.test_cake = Cake(self, 'test cake')
		#self.test_cake.ingredients.add(Ingredient(self, 'test ingredient', WIDTH + 20, 20, protein=20))
		#self.test_cake.ingredients.add(Ingredient(self, 'test ingredient2', WIDTH + 20, 60, protein=13))
		#self.all_cakes.add(self.test_cake)


		#--------------------SAVING MODULE TESTS
		#self.mem = Memory(self)
		#self.mem.save(self.test_cake)
		#loaded = self.mem.load('save.obj')
		#self.cake1 = self.mem.recreate_obj(loaded)


		#self.all_cakes.add(self.cake1)


		#TEST -------------------------------------SAVING MODULE 2 TESTS---------------------------------TEST

		print('TESTY PROJECT CREATORA--------------')

		# ### Create cake with ingredient with protein
		# print()
		# print('Project creating test part --->')
		# self.test_cake = Cake(self, 'test cake save module')
		# self.test_cake.ingredients.add(Ingredient(self, 'test ingredient save mod', WIDTH + 20, 20, protein=20))
		# self.test_cake.ingredients.add(Ingredient(self, 'test ingredient2, save mod', WIDTH + 20, 60, protein=13))
		# self.all_cakes.add(self.test_cake)


		# self.lop = ListOfProjects()

		# # Creating project
		# self.pc = ProjectCreator()
		# self.tp = self.pc.create_project('first project')
		# self.lop.projects.append(self.tp)
		# #self.current_project = self.tp

		# # Set all cakes to current project cakes
		# #self.current_project.cakes = self.all_cakes
		# #print('ciasta obecnego projektu: ', str(self.current_project.cakes))

		# #self.lop.projects.append(ProjectCreator().create_project('first project'))
		# print()
		# print('Project saving tests --->')
		# print(str(self.lop.projects))
		# self.ps = ProjectSaver(self)
		# #self.ps.save()


		# # ---LOADING PART
		# print()
		# print('Project loader tests --->')
		# self.pl = ProjectLoader(self)
		# self.pl.load_all_projects()
		# #self.pl.load_all_projects('/blabla/ble')





		print('KONIEC TESTOW-----------------')

		


		# ----------------- Running the main program

		# Start screen
		#self.start_screen()

		# Creator screen
		#self.project_creator_screen()

		# Cake screen
		self.run()




	def run(self):
		# Loop that will controll all loops (screens)
		self.control_loop = True
		while self.control_loop:
			# Start Screen
			if self.current_screen == "main_screen":
				# Clear all cakes group
				self.all_cakes.empty()
				# Load project cakes for main screen
				for cake in self.current_project.cakes:
					self.all_cakes.add(cake)
					
				# Run main Screen
				self.running = True
				while self.running:
					self.clock.tick(FPS)
					self.events()
					self.update()
					self.draw()
					#print("Current Screen: ", str(self.current_screen))

			# Run start Screen	
			if self.current_screen == "start_screen":
				self.start_screen()
				#print("Current Screen: ", str(self.current_screen))
			# Run create screen
			if self.current_screen == "create_screen":
				self.project_creator_screen()
				#print("Current Screen: ", str(self.current_screen))

			# Update current scrren number (if not, the screen will not change)
			self.current_screen = self.screens[self.screen_number]




	def events(self):
		# Check for quit event
		check_for_events(self)

		# Mouse position
		self.mouse_pos = pg.mouse.get_pos()
		#print(self.mouse_pos)


	def update(self):	 


		self.all_sprites.update()

		# Cake list handling objects one under another	
		self.all_cakes.update()

		# Scrollers update
		self.scrollers.update()

		# Arrows update
		self.arrows.update()

		# Cake ingredients update
		for cake in self.all_cakes:
			for ingr in cake.ingredients:
				ingr.update()
			
		# Coursor colision with cakes
		cake_hits = pg.sprite.spritecollide(self.mouse, self.all_cakes, False)
		if cake_hits:
			for cake in cake_hits:
				for active_cake in self.all_cakes:
					active_cake.is_highlighted = False
				cake.is_highlighted = True
		else:
			for cake in self.all_cakes:
				cake.is_highlighted = False




		# Computing an amount of macros for cake 
		for cake in self.all_cakes:
			cake.count_macros()


		# Using list object to set up limited cake list do display
		self.list.select_objects(self.all_cakes)
		# Draw List object collection of cakes

		# Get list of cakes with modified position of items that are out of display range
		self.all_cakes = self.list.set_out_of_list()


		# Ingredients list scrolling ----------------INGREDIENTS LIST SCROLLING
		# list of ingredients of curently selected cake
		self.current_cake_ingrs = []
		# Checking if page number is 2		
		if self.current_page == 2:
			# Checkig wich cake is active
			for cake in self.all_cakes:
				if cake.is_active:
					#print('Cake is Active: ' + str(cake.name))
					# Check if there are any ingredients to deal with
					if len(cake.ingredients) > 0:
						# Selecting limited amount of objects
						self.ingredients_collection.select_objects(cake.ingredients)
						# Get list of ingredients with modified position of items that are out of display range
						cake.ingredients = self.ingredients_collection.set_out_of_list()
					# If there is no ingredients in selected cake, we need to clear a list
					elif len(cake.ingredients) == 0:
						self.ingredients_collection = List(self)


						# print('Cake ingredients: ' + str(cake.ingredients))
						# print('Selected objects: ' + str(self.ingredients_collection))
						# print('Items out of list: ' + str(cake.ingredients))

		# Ingredients button bug fix
		# Fix bug for ingredients button Ugly
		if self.current_page == 1:
			for button in self.ingredients_collection.buttons:
				button.kill()
				
		
		



		#----------------------------------------------------------------------------UPDATE DEBUG
		#print('CURRENT PAGE: ' + str(self.current_page))

	def draw(self):
		# Filling with color OBLIGATORY
		self.screen.fill(BLACK)

		# Drawing general
		self.all_sprites.draw(self.screen)
		#self.all_cakes.draw(self.screen)

		# Draw scrollers
		# Only on page 2
		if self.current_page == 2:
			if self.scroller.is_active:
				self.scrollers.draw(self.screen)
				# draw text for scroller
				self.scroller.display_item()
				# Draw arrows
				self.arrows.draw(self.screen)


		
		#Input text drawing
		# one page one:
		if self.current_page == 1:
			draw_input_text(self,
							self.screen,
							self.input.input_str, 
							self.input.rect.x, 
							self.input.rect.y, 
							PINK, 
							20, 
							coursor=self.input.coursor)
		elif self.scroller.is_editable:
			draw_input_text(self,
							self.screen,
							self.input.input_str, 
							self.scroller.rect.x, 
							self.scroller.rect.y + 15, 
							PINK, 
							20, 
							coursor=self.input.coursor)


		# Show cake ingredients 
		#for cake in self.all_cakes:
			#if cake.is_active:
			#	cake.ingredients.draw(self.screen)
				#show ingredient name
			#	for ingr in cake.ingredients:
			#		ingr.draw_text()
			#		ingr.show_details() # Shows detail of ingredients
		

		# Drawing CakeGeneral details
		self.cakegeneral.show_details()

		# ---------------------------------------------CAKE LIST DROWING SECTION -----------------------------------------------
		
		# Draw List object collection of cakes
		# Get list of cakes to display
		cakes = self.list.update_given_collection()
		# Get list of cakes with modified position of items that are out of display range
		#self.all_cakes = self.list.set_out_of_list()
		cakes.draw(self.screen)
		# Draw text for all cakes
		for cake in cakes:
			cake.draw_text()
		# Draw list buttons
		self.list.buttons_to_draw().draw(self.screen)

		# ---------------------------------------------CAKE INGREDIENTS LIST DROWING SECTION -----------------------------------------------
		#if self.current_page == 2:
		for cake in self.all_cakes:
			if cake.is_active:
				try:
					ingrs = self.ingredients_collection.update_given_collection()
					# Draw updated collection
					ingrs.draw(self.screen)
					# Draw text on items
					#ingrs.draw_text()
					# Draw informations about ingredient
					for ingr in ingrs:
						ingr.draw_text()
						ingr.show_details()
					self.ingredients_collection.buttons_to_draw().draw(self.screen)
				except:
					pass



		
	
		


		

		# Updating the screen
		pg.display.update()

	
	#-------------------------------------------------------------START SCREEN ------------------------------
	
	def start_screen(self):
		# Creating all items for start screen
		self.create_start_items()
		
		# Start main start screen loop
		self.start_running = True
		while self.start_running:
			self.clock.tick(FPS)
			# Events
			self.start_events()

			# Update
			self.start_update()


			# Draw
			self.start_draw()
			

		# When you click create button precedent loop ends
		# Creator screen
		#self.project_creator_screen()

	def start_events(self):
		'''
		Checking for events in start screen
		'''
		# Get mouse position
		self.mouse_pos = pg.mouse.get_pos()

		print('screen number: ', str(self.screen_number))

		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.start_running= False
				self.control_loop = False
				#self.start_running= False
				#self.current_screen = 2
				
			# Check for keyboard for typing letters ---------------------- TYPING LETTERS
			if event.type == pg.KEYDOWN:
				print('START SCREEN WORKS')

			# Checking for mouse click ------------------------------MOUSE CLICK
			if event.type == pg.MOUSEBUTTONUP:
				# chceck for hits with menu items
				hits = pg.sprite.spritecollide(self.start_mouse, self.all_start_sprites, False)
				if hits:
					# Check witch button was pressed 
					# Case 1 - Load project button
					if hits[0].name == 'start':
						# Pass the selected project to main screen project
						# If project was selected load it, and go to main screen
						if len(self.scroll_list_display.selected_project) > 0:
							self.current_project =  self.scroll_list_display.selected_project[0]
							# Set new screen number to number of main screen
							self.screen_number = 2
							# Exit start screen
							self.start_running = False
					# Case 2 - Create button
					if hits[0].name == 'create':
						print("Create button was clicked")
						# Set new screen number to number of create screen
						self.screen_number = 1
						# Exit start screen
						self.start_running = False


						
					
				

				# Check if we clicked on project
				for project in self.scroll_list_display.get_projects_to_display():
					# Check for collisions with mouse
					if  project.rect.x + project.rect.width > self.mouse_pos[0] > project.rect.x and project.rect.y+ project.rect.height > self.mouse_pos[1] > project.rect.y:
						# Deselect all projects
						#for project in self.scroll_list_display.get_projects_to_display():
							#if project.is_selected == True:
								#project.is_selected = False
								
								#break
						# Select project
						project.is_selected = True
						self.scroll_list_display.selected_project.append(project)
						print('Click')
						
					
					#break

						#print()	 
						#print('Project clicked: ', str(project))
			
		
					
					



		
		#print(self.mouse_pos) 

	def start_update(self):
		'''
		Updating start menu elements
		'''
		
		# Updating all sprites for start screen
		self.all_start_sprites.update()

		# Mouse update
		self.start_mouse_group.update()

		# TEST UPDATE
		# scroll display lis
		#self.scroll_list_display.draw(self.screen)
		self.test_draw.update()

		# Update projects
		self.scroll_list_display.get_projects_to_display().update()

		# Fill curently selected project with color
		if len(self.scroll_list_display.selected_project) > 0:
			self.scroll_list_display.selected_project[0].image.fill(GREEN)




	def start_draw(self):
		'''
		Drawing start menu elements
		'''


		# Filling with color OBLIGATORY
		self.screen.fill(MENU_BACKGROUND_COLOR)



		# Draw start menu elements

		# Draw all sprites
		self.all_start_sprites.draw(self.screen)

		# Draw mouse
		self.start_mouse_group.draw(self.screen)

		# Drawing discription on a screen
		for item in self.all_start_sprites:
			try:
				item.draw_text(self.screen)
			except:
				continue

		# Title
		start_text(40, 20, self.screen, TITLE, 70, font_name='Tahoma', is_Bold=False, color=LILA)


		# TEST DRAW
		# scroll display lis
		#self.scroll_list_display.draw(self.screen)
		self.test_draw.draw(self.screen)
		# draw projects 
		self.scroll_list_display.get_projects_to_display().draw(self.screen)
		self.scroll_list_display.draw_border(self.screen, WHITE)
		# draw projects name
		for i in self.scroll_list_display.get_projects_to_display():
			i.display_text(self.screen)




		





		# Updating the screen
		pg.display.update()






	def create_start_items(self):
		'''
		Creating all items for start screen
		'''

		# ------------FILE LOADER -----------
		print()
		print('START PRAWDZIWYCH TESTOW -------------')
		print()
		print('REAL project loader test START---->')
		# Creating project loader object
		self.project_loader = ProjectLoader(self)
		# Loading projects from files 
		self.project_loader.load_all_projects()
		print('Projects loaded: ', str(self.project_loader.all_loaded_projects))
		

		# ----------ITEM CREATION-----------

		# Creating start button
		self.start = Start(self, 40, 120, LOAD_BUTTON_TEXT)
		self.create = Create(self, 40, 170, CREATE_BUTTON_TEXT)

		# Creating mouse
		self.start_mouse = Mouse(self)

		# Creating Scroll List Display
		self.scroll_list_display = ScrollListDisplay(self, self.project_loader.all_loaded_projects, self.screen)

		# SideBar <--TEST
		self.side_bar = SideBar(self,
								20, 
								60, 
								collection=self.scroll_list_display.sprite_group, 
								attached_to=self.scroll_list_display )

		# Creating project
		#self.project = Project(self, WIDTH/2, HEIGHT/2, 300, 75, BLACK, 'project')
		


		# ------------GROUPS-----------------
		
		# Groups for start menu
		self.all_start_sprites = pg.sprite.Group()
		self.start_mouse_group = pg.sprite.Group()

		# TEST GROUP
		self.test_draw = pg.sprite.Group()
		self.test_draw.add(self.scroll_list_display)


		
		# Adding buttons  to the groups
		self.all_start_sprites.add(self.start)
		self.all_start_sprites.add(self.create)

		# Add sidebar to the group <--TEST
		self.all_start_sprites.add(self.side_bar)



		
			

		

		


		# Adding mouse to the groups
		self.start_mouse_group.add(self.start_mouse)

		# Adding projects to the group
		#self.all_start_sprites.add(self.project)






	# -------------------------------------------- PROJECT CREATOR SECTION ---------------


	def project_creator_screen(self):
		'''
		Screen for creating projects
		'''
		

		# creating all objects for creator screen
		self.create_creator_items()


		# Start main  project creator screen loop
		self.creator_running = True
		while self.creator_running:
			self.clock.tick(FPS)
			# Events
			self.creator_events()

			# Update
			self.creator_update()


			# Draw
			self.creator_draw()
			#print("Current Screen: ", str(self.current_screen))


		# Sets control variable to false
		self.is_creating = False


	def creator_events(self):
		'''
		Checking for events in project creator screen
		'''
		# Check for keyboard events
				
		check_for_keyboard_input(self)
			

			


		# Get mouse position
		self.mouse_pos = pg.mouse.get_pos()

	def creator_update(self):
		'''
		Updating creator menu elements
		'''
		
		# Updating all sprites for start screen
		self.all_creator_sprites.update()

		# Input update
		self.input.update()

		# Mouse update
		self.creator_mouse_group.update()




	def creator_draw(self):
		'''
		Drawing start menu elements
		'''


		# Filling with color OBLIGATORY
		self.screen.fill(MENU_BACKGROUND_COLOR)



		# Draw create menu elements

		# Draw input text
		draw_input_text(self,
					self.screen, 
					self.input.input_str, 
					20, 
					20, 
					VIOLET, 
					40,
					coursor=self.input.coursor,
					hint1='Podaj nazwe nowego projektu',
					hint2='Podaj nazwe nowego projektu',
					hint3='Podaj nazwe nowego projektu',
					hint4='Podaj nazwe nowego projektu',
					hint5='Podaj nazwe nowego projektu',)

		# Draw all sprites
		self.all_creator_sprites.draw(self.screen)

		# Draw mouse
		self.creator_mouse_group.draw(self.screen)

		# Draw create button text
		try: 
			self.cpbutton.draw_text(self.screen)
		except:
			pass


		

		


		





		# Updating the screen
		pg.display.update()


	def create_creator_items(self):
		'''
		Creating all items for start screen
		'''
		
		# ------------GROUPS------------
		
		# Groups for start menu
		self.all_creator_sprites = pg.sprite.Group()
		self.creator_mouse_group = pg.sprite.Group()

		# Adding input to a the group
		#self.all_creator_sprites.add(self.input)


		# ----------ITEM CREATION-----------

		# Creating  button

		# Project creator button
		self.cpbutton = CreateProjectButton(self)
		
		

		# Creating mouse
		self.creator_mouse = Mouse(self)

		# Creating project
		





		# ----------ADDING TO THE GROUPS ----------

		
		# Adding buttons  to the groups
		

		# Adding mouse to the groups
		self.all_creator_sprites.add(self.cpbutton)
		self.creator_mouse_group.add(self.creator_mouse)

		# Creating project
		self.project = Project(self, WIDTH/2, HEIGHT/2, 300, 75, BLACK, 'project')

		# Adding projects to the group
		print('project creator lounched-end- default project created')


		# Sets control variable to true
		self.is_creating = True

		
		



		


		




if __name__ == '__main__':
	mc = MagicCake()
	mc.new()
	pg.quit()