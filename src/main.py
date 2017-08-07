import pygame as pg

from remember import *
from settings import *
from sprites import *
from utils import *
from start import *


class MagicCake:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		self.clock = pg.time.Clock()
		# Inital mouse  position
		self.mouse_pos = pg.mouse.get_pos()

		# Pagination pages
		self.current_page = 1


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
		
		# ingredients list
		self.ingredients_collection = List(self)		


		#--------------------------------TEST--------------------------------------------------------------------
		### Create cake with ingredient with protein
		self.test_cake = Cake(self, 'test cake')
		self.test_cake.ingredients.add(Ingredient(self, 'test ingredient', WIDTH + 20, 20, protein=20))
		self.test_cake.ingredients.add(Ingredient(self, 'test ingredient2', WIDTH + 20, 60, protein=13))
		self.all_cakes.add(self.test_cake)


		#--------------------SAVING MODULE TESTS
		self.mem = Memory(self)
		self.mem.save(self.test_cake)
		loaded = self.mem.load('save.obj')
		self.cake1 = self.mem.recreate_obj(loaded)


		self.all_cakes.add(self.cake1)
		


		# Running the main propgram
		self.start_screen()
		self.run()


	def run(self):
		self.running = True
		while self.running:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()


	def events(self):
		# Check for quit event
		check_for_events(self)

		# Mouse position
		self.mouse_pos = pg.mouse.get_pos()
		print(self.mouse_pos)


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
					print('Cake is Active: ' + str(cake.name))
					# Check if there are any ingredients to deal with
					if len(cake.ingredients) > 0:
						# Selecting limited amount of objects
						self.ingredients_collection.select_objects(cake.ingredients)
						# Get list of ingredients with modified position of items that are out of display range
						cake.ingredients = self.ingredients_collection.set_out_of_list()
					# If there is no ingredients in selected cake, we need to clear a list
					elif len(cake.ingredients) == 0:
						self.ingredients_collection = List(self)


						print('Cake ingredients: ' + str(cake.ingredients))
						print('Selected objects: ' + str(self.ingredients_collection))
						print('Items out of list: ' + str(cake.ingredients))

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

	def start_events(self):
		'''
		Checking for events in start screen
		'''
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.start_running= False
				
			# Check for keyboard for typing letters
			if event.type == pg.KEYDOWN:
				print('START SCREEN WORKS')

		# Get mouse position
		self.mouse_pos = pg.mouse.get_pos()
		print(self.mouse_pos) 

	def start_update(self):
		'''
		Updating start menu elements
		'''
		
		# Updating all sprites for start screen
		self.all_start_sprites.update()

		



	def start_draw(self):
		'''
		Drawing start menu elements
		'''


		# Filling with color OBLIGATORY
		self.screen.fill(MENU_BACKGROUND_COLOR)



		# Draw start menu elements

		# Draw all sprites
		self.all_start_sprites.draw(self.screen)

		# Title
		start_text(40, 20, self.screen, TITLE, 70, font_name='Tahoma', is_Bold=False, color=LILA)

		





		# Updating the screen
		pg.display.update()

	def create_start_items(self):
		'''
		Creating all items for start screen
		'''
		
		# Groups for start menu
		self.all_start_sprites =pg.sprite.Group()


		# Creating start button
		self.start = Start(self, 40, 120)

		self.start_mouse = Mouse(self)

		# Adding items to the gropus
		self.all_start_sprites.add(self.start)
		self.all_start_sprites.add(self.start_mouse)
		





		




if __name__ == '__main__':
	mc = MagicCake()
	mc.new()
	pg.quit()