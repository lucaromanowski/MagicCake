import pygame as pg

from settings import *
from sprites import *
from utils import *


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
		
		#--------------------------------TEST--------------------------------------------------------------------
		### Create cake with ingredient with protein
		self.test_cake = Cake(self, 'test cake')
		self.test_cake.ingredients.add(Ingredient(self, 'test ingredient', WIDTH + 20, 20, protein=20))
		self.test_cake.ingredients.add(Ingredient(self, 'test ingredient2', WIDTH + 20, 60, protein=13))
		self.all_cakes.add(self.test_cake)

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




		# Computing an amount of proteins for cake ---------------> THIS SHOUD COMPUTE ALL INGREDIENTS VALUES NOT ONLY PROTEIN
		for cake in self.all_cakes:
			cake.count_macros()


		# Using list object to display cake list
		self.list.select_objects(self.all_cakes)





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

		#
		#for cake in self.all_cakes:
			#cake.draw_text() #self.all_cakes.draw_text()
		
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
		for cake in self.all_cakes:
			if cake.is_active:
				cake.ingredients.draw(self.screen)
				#show ingredient name
				for ingr in cake.ingredients:
					ingr.draw_text()
					ingr.show_details() # Shows detail of ingredients
		

		# Drawing CakeGeneral details
		self.cakegeneral.show_details()

		# ---------------------------------------------CAKE LIST DROWING SECTION -----------------------------------------------
		
		# Draw List object collection of cakes
		# Get list of cakes to display
		cakes = self.list.update_given_collection()
		# Get list of cakes with modified position of items that are out of display range
		self.all_cakes = self.list.set_out_of_list()
		cakes.draw(self.screen)
		# Draw text for all cakes
		for cake in cakes:
			cake.draw_text()
		# Draw list buttons
		self.list.buttons_to_draw().draw(self.screen)

		
	



		# Updating the screen
		pg.display.update()

if __name__ == '__main__':
	mc = MagicCake()
	mc.new()
	pg.quit()