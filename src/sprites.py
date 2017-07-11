import pygame as pg
import random

from settings import *

vec = pg.math.Vector2



class Input(pg.sprite.Sprite):
	def __init__(self, magiccake):
		pg.sprite.Sprite.__init__(self)
		self.MagicCake = magiccake
		self.image = pg.Surface((440, 30))
		#self.image.fill(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 20
		self.rect.y = 20 

		# Text and coursor
		self.input_list = []
		self.input_str = ''
		self.coursor = COURSOR
		self.coursor_blink_freq = COURSOR_BLINK_FREQ 

	def update(self):       	
		# We are checking for typing letters in main.events
		# Update the string of ingrName
		#if self.MagicCake.current_page == 1:
		self.input_str = ''.join(self.input_list)
		# Capitalize
		self.input_str = self.input_str.capitalize()

		# Blinking coursor
		self.coursor_blink_freq += 1
		if self.coursor_blink_freq > 10:
			self.coursor = ''
			if self.coursor_blink_freq > 20:
				self.coursor_blink_freq = 0
		if self.coursor_blink_freq < 10:
			self.coursor = COURSOR


		# DEBUG ---------------------------------------------------------------------------------------DEBUG
		#print(self.input_str)
		#print(self.input_list)
		#print(len(self.input_list))
		#print(self.coursor)


class Cake(pg.sprite.Sprite):
	def __init__(self, magiccake, name):
		pg.sprite.Sprite.__init__(self)
		self.MagicCake = magiccake
		self.image = pg.Surface((200, 30))
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = WIDTH - 220
		self.rect.y = 20
		self.is_highlighted = False
		self.is_active = False

		self.name = name
		
		# List of ingredient objects
		self.ingredients = pg.sprite.Group()

		# Basic info
		self.protein = 0
		self.carb = 0
		self.fat = 0
		self.kcal = 0
		self.price = 0

		# Movement 
		self.pos = vec(WIDTH - 220, 20)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)

		self.is_moving = False

	def count_protein(self):
		# Setting cake protein amount
		protein = 0
		for ingr in self.ingredients:
			protein += ingr.protein
			#print('Protein: ' + str(self.protein))
		self.protein = protein

	def count_macros(self):
		'''
		Count all makros for cake. values based on ingredient's properties (ingredient's macros)
		'''
		# Setting cake protein amount
		protein = 0
		for ingr in self.ingredients:
			protein += ingr.given_protein
			#print('Protein: ' + str(self.protein))
		self.protein = protein

		# Setting cake carb amount
		carb = 0
		for ingr in self.ingredients:
			carb += ingr.given_carb
			#print('Protein: ' + str(self.protein))
		self.carb = carb

		# Setting cake fat amount
		fat = 0
		for ingr in self.ingredients:
			fat += ingr.given_fat
			#print('Protein: ' + str(self.protein))
		self.fat = fat

		# Setting cake kcal amount
		kcal = 0
		for ingr in self.ingredients:
			kcal += ingr.given_kcal
			#print('Protein: ' + str(self.protein))
		self.kcal = kcal

		# Setting cake price 
		price = 0
		for ingr in self.ingredients:
			price += ingr.given_price
			#print('Protein: ' + str(self.protein))
		self.price = price



	def update(self):
		# Check for collision with difrent all_cakes objects
		self.check_for_hits = True
		while self.check_for_hits:
			hits = pg.sprite.spritecollide(self, self.MagicCake.all_cakes, False)
			if hits:
				# Checking for not colliding with self
				if self != hits[0]:
					self.rect.y = hits[0].rect.bottom + 10
				else:
					self.check_for_hits = False
		
		# Setting background color depending on status (highlighted, active)
		# Highlighted
		if self.is_highlighted:
			self.image.fill(RED)
		else:
			self.image.fill(WHITE)

		# Acitve	
		if self.is_active:
			self.image.fill(BLUE)
		#else:
			#self.image.fill(WHITE)

		# Active and highlighted
		if self.is_active and self.is_highlighted:
			self.image.fill(SELEDIN)

		# Movement
		#self.acc += self.vel * FRICTION
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc

		self.rect.x = self.pos.x

		# Stop it!
		# Left
		if self.pos.x <= - 300:
			self.vel = vec(0, 0)
			self.acc = vec(0, 0)
			self.pos.x = - 300 + 1
			self.is_moving = False
		
		# Right
		if self.pos.x >= WIDTH - 220:
			self.vel = vec(0, 0)
			self.acc = vec(0, 0)
			self.pos.x = WIDTH - 220
			self.is_moving = False

		# -----------------------------------------------------------------MOVEMENT DEBUG
		#print('ACC: ' + str(self.acc))
		#print('VEL: ' + str(self.vel))
		#print('POS: ' + str(self.pos))
		#print('SELF MOVING: ' + str(self.is_moving))
		#print('ACC: ' str(self.acc))


	



		#print(str(self.is_active))

	def draw_text(self):
		COL = RED
		if self.is_highlighted:
			COL = GREEN
		if self.is_active and self.is_highlighted:
			COL = WHITE
		# Drawing cakes name
		# Drawing text inside of self surface
		# Select the font to use, size, bold, italics
		font = pg.font.SysFont('Courier', 18, False, False)
		 
		# Render the text. "True" means anti-aliased text.
		# Black is the color. The variable BLACK was defined
		# above as a list of [0, 0, 0]
		# Note: This line creates an image of the letters,
		# but does not put it on the screen yet.
		text = font.render(self.name, True, COL)
		 
		# Put the image of the text on the screen at 250x250
		self.MagicCake.screen.blit(text, [self.rect.x + 3, self.rect.y + 4])


class Ingredient(pg.sprite.Sprite):
	def __init__(self, magiccake, name, x, y, how_much=0, protein=0, carb=0, fat=0, kcal=0, package_size=0, price=0):
		pg.sprite.Sprite.__init__(self)
		self.MagicCake = magiccake
		self.name = name
		self.how_much = how_much
		self.protein = protein
		self.carb = carb
		self.fat = fat
		self.kcal = kcal
		self.package_size = package_size
		self.price = price

		# Macros for given amount (WARRNING: 0 division possible)
		self.given_protein = 0
		self.given_carb = 0
		self.given_fat = 0
		self.given_kcal = 0
		self.given_price = 0

		# List used for scroller
		self.scroll_list = [self.name, 
							self.how_much, 
							self.protein, 
							self.carb, 
							self.fat, 
							self.kcal, 
							self.package_size,
							self.price
							]

		self.image = pg.Surface((200, 30))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()

		# Animation
		self.pos = vec(x, y)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)

		self.is_highlighted = False
		self.is_active = False

	def update(self):
		# Check for ingr collide with coursor
		hits = pg.sprite.collide_rect(self, self.MagicCake.mouse)
		if hits:
			self.is_highlighted = True
		else:
			self.is_highlighted = False


		# Movement
		#print('INGREDIENT SHOULD BE ON THE SCREEN IN GREEN COLOR')
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc

		self.rect.x = self.pos.x
		self.rect.y = self.pos.y

		# Stop it!
		# Left
		if self.pos.x <= 20:
			self.vel = vec(0, 0)
			self.acc = vec(0, 0)
			self.pos.x = 20
		
		# Right
		if self.pos.x >= WIDTH + 220:
			self.vel = vec(0, 0)
			self.acc = vec(0, 0)
			self.pos.x = WIDTH + 220

		# Setting background color depending on status (highlighted, active)
		# Highlighted
		if self.is_highlighted:
			self.image.fill(RED)
		else:
			self.image.fill(GREEN)

		# Acitve	
		if self.is_active:
			self.image.fill(BLUE)

		#else:
			#self.image.fill(WHITE)

		# Active and highlighted
		if self.is_active and self.is_highlighted:
			self.image.fill(SELEDIN)

		# Update list (Scroller object needs this list to be up to date)
		self.scroll_list = [self.name, 
							self.how_much, 
							self.protein, 
							self.carb, 
							self.fat, 
							self.kcal,
							self.package_size, 
							self.price]

		# Update given macros amounts (try for zero division case)
		# Protein
		try:
			self.given_protein = self.protein/100 * self.how_much
		except ValueError:
			pass

		# Carb
		try:
			self.given_carb = self.carb/100 * self.how_much
		except ValueError:
			pass

		# Fat
		try:
			self.given_fat = self.fat/100 * self.how_much
		except ValueError:
			pass

		# Kcal
		try:
			self.given_kcal = self.kcal/100 * self.how_much
		except ValueError:
			pass

		# Price
		try:
			self.given_price = (self.how_much / self.package_size) * self.price
		except ZeroDivisionError:
			pass

		print('SELECTED INGREDIENT STATUS: ' + str(self.is_active))

	def move(self, dir):
		if dir == 'left':
			self.acc -= vec(random.randrange(6, 8), 0)

		elif dir == 'right':
			self.acc += vec(random.randrange(6, 8), 0)

	def draw_text(self):
		'''
		Drawing informations about ingredient
		
		'''

		# Drawing ingredient name on rect
		font = pg.font.SysFont('Courier', 16, False, False)
				 
		# Render the text. "True" means anti-aliased text.
		# Black is the color. The variable BLACK was defined
		# above as a list of [0, 0, 0]
		# Note: This line creates an image of the letters,
		# but does not put it on the screen yet.
		text_name = font.render(str(self.name), True, WHITE)
		
		self.MagicCake.screen.blit(text_name, [self.rect.x + 3, self.rect.y + 4])

		 
		# Put the image of the text on the screen

	def show_details(self):
		if self.is_highlighted or self.is_active:
			print("details of INGREDIENTS")
			# Drawing ingredient name on rect
			font = pg.font.SysFont('Courier', 16, False, False)

						 
				# Render the text. "True" means anti-aliased text.
				# Black is the color. The variable BLACK was defined
				# above as a list of [0, 0, 0]
				# Note: This line creates an image of the letters,
				# but does not put it on the screen yet.

			# TEXTS TO BLIT:	
			t_title = font.render("Zawartosc w 100g: ", True, WHITE)
			t_how_much = font.render("Ilość produktu: " + str(self.how_much) + " g", True, WHITE)
			t_protein = font.render("Białko: " + str(self.protein) + " g", True, WHITE)
			t_carb = font.render("Węglowodany: " + str(self.carb) + " g", True, WHITE)
			t_fat = font.render("Tłuszcz: " + str(self.fat) + " g", True, WHITE)
			t_kcal = font.render("Kalorie: " + str(self.kcal) + " kcal", True, WHITE)
			t_price = font.render("Cena: " + str(self.price) + " zl", True, WHITE)

			# Text for macros value for given amount of product
			given_title= font.render("Makro dla danej ilości: ", True, WHITE)
			t_package_size = font.render("Opakowanie na: " + str(self.package_size) + " g", True, WHITE)
			given_protein = font.render("Białko: {0:.2f} g".format(self.given_protein), True, WHITE)
			given_carb = font.render("Węgle: {0:.2f} g".format(self.given_carb), True, WHITE)
			given_fat = font.render("Tłuszcz: {0:.2f} g".format(self.given_fat), True, WHITE)
			given_kcal = font.render("Kalorie: {0:.2f} g".format(self.given_kcal), True, WHITE)
			given_price = font.render("Koszt jednostkowy: {0:.2f} g".format(self.given_price), True, WHITE)
			
			self.MagicCake.screen.blit(t_title, [WIDTH - 200, 40])		
			self.MagicCake.screen.blit(t_how_much, [WIDTH - 450, 40])
			self.MagicCake.screen.blit(t_protein, [WIDTH - 200, 80])
			self.MagicCake.screen.blit(t_carb, [WIDTH - 200, 120])
			self.MagicCake.screen.blit(t_fat, [WIDTH - 200, 160])
			self.MagicCake.screen.blit(t_kcal, [WIDTH - 200, 200])
			self.MagicCake.screen.blit(t_price, [WIDTH - 450, 80])

			# Display for given amounts of macros
			self.MagicCake.screen.blit(given_title, [WIDTH - 270, 320])
			self.MagicCake.screen.blit(t_package_size, [WIDTH - 270, 360])
			self.MagicCake.screen.blit(given_protein, [WIDTH - 270, 400])
			self.MagicCake.screen.blit(given_carb, [WIDTH - 270, 440])
			self.MagicCake.screen.blit(given_fat, [WIDTH - 270, 480])
			self.MagicCake.screen.blit(given_kcal, [WIDTH - 270, 520])
			self.MagicCake.screen.blit(given_price, [WIDTH - 270, 560])

	def set_name(self, name):
		self.name = name

	def set_how_much(self, how_much):
		self.how_much = how_much
	
	def set_protein(self, protein):
		self.protein = protein
	
	def set_carb(self, carb):
		self.carb = carb
	
	def set_fat(self, fat):
		self.fat = fat
	
	def set_kcal(self, kcal):
		self.kcal = kcal

	def set_price(self, price):
			self.price = price

class Mouse(pg.sprite.Sprite):
	def __init__(self, magiccake):
		pg.sprite.Sprite.__init__(self)
		self.MagicCake = magiccake
		self.image = pg.Surface((10, 10))
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.rect.x = self.MagicCake.mouse_pos[0]
		self.rect.y = self.MagicCake.mouse_pos[1]

	def update(self):
		self.rect.x = self.MagicCake.mouse_pos[0]
		self.rect.y = self.MagicCake.mouse_pos[1]


class CakeGeneral(pg.sprite.Sprite):
	def __init__(self, magiccake):
		pg.sprite.Sprite.__init__(self)
		self.MagicCake = magiccake
		self.image = pg.Surface((800, 500))
		self.image.fill(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 20
		self.rect.y = 60
		self.is_active = False

		# Movement 
		self.pos = vec(20, 60)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)
		

	def update(self):
		# Movement
		#self.acc += self.vel * FRICTION
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc

		self.rect.x = self.pos.x

		# Stop it!
		# Left
		if self.pos.x <= -900:
			self.vel = vec(0, 0)
			self.acc = vec(0, 0)
			self.pos.x = -900 
			#self.is_moving = False
		
		# Right
		if self.pos.x >= 20:
			self.vel = vec(0, 0)
			self.acc = vec(0, 0)
			self.pos.x = 20 
			#self.is_moving = False

		# Check if any cake is selected
		for cake in self.MagicCake.all_cakes:
			if cake.is_active:
				self.is_active = True
				# Only one cake can be selected, there is no need to perform more tests
				break
			else:
				self.is_active = False

		# Setting background color white to show a Rect	when cake is selected
		#if self.is_active:
			#.image.fill(WHITE)
		#else:
			#self.image.fill(BLACK)

	def show_details(self):
		# Check if any cake is active:
		for cake in self.MagicCake.all_cakes:
			if cake.is_active:

				#Creating list of ingredients 
				ingr_list = [i.name for i in cake.ingredients]
				ingr_str = ", ".join(ingr_list)
				#print('TO JEST LIST KOMPREHENCJA: ' + ingr_str)

				# name, ingredients,

				# Drawing cakes name
				# Drawing text inside of self surface
				# Select the font to use, size, bold, italics
				header_font = pg.font.SysFont('Courier', 22, False, False)
				font = pg.font.SysFont('Courier', 16, False, False)
				 
				# Render the text. "True" means anti-aliased text.
				# Black is the color. The variable BLACK was defined
				# above as a list of [0, 0, 0]
				# Note: This line creates an image of the letters,
				# but does not put it on the screen yet.
				text_name = header_font.render('Ciasto: ' + cake.name, True, WHITE)
				text_ingr_header = font.render('Podstawowe informacje: ', True, WHITE)
				


				
				# Showing basic cake infos
				text_protein = font.render('Bialko: {0:.2f} g'.format(cake.protein), True, WHITE)
				text_carb = font.render('Weglowodany: {0:.2f} g'.format(cake.carb), True, WHITE)
				text_fat = font.render('Tluszcze: {0:.2f} g'.format(cake.fat), True, WHITE)
				text_kcal = font.render('Kalorie: {0:.2f} kcal'.format(cake.kcal), True, WHITE)
				text_price = font.render('Cena: {0:.2f} zl'.format(cake.price), True, WHITE)

				# text for list of all ingredients
				text_ingr = font.render("Wszystkie składniki: ", True, WHITE)
				text_ingr_list = font.render(ingr_str, True, WHITE)


				# Put the image of the text on the screen
				self.MagicCake.screen.blit(text_name, [self.rect.x + 3, self.rect.y + 4])
				self.MagicCake.screen.blit(text_ingr_header, [self.rect.x + 3, self.rect.y + 34]) #+30px


				space = 65
				self.MagicCake.screen.blit(text_protein, [self.rect.x + 3, self.rect.y + space])
				space += 35 
				self.MagicCake.screen.blit(text_carb, [self.rect.x + 3, self.rect.y + space]) 
				space += 35
				self.MagicCake.screen.blit(text_fat, [self.rect.x + 3, self.rect.y + space]) 
				space += 35
				self.MagicCake.screen.blit(text_kcal, [self.rect.x + 3, self.rect.y + space]) 
				space += 35
				self.MagicCake.screen.blit(text_price, [self.rect.x + 3, self.rect.y + space]) 
				space += 35
				
				# Show ingredients list on the screen
				space += 35
				self.MagicCake.screen.blit(text_ingr, [self.rect.x + 3, self.rect.y + space]) 
				space += 35
				self.MagicCake.screen.blit(text_ingr_list, [self.rect.x + 3, self.rect.y + space]) 
					

class Paginator(pg.sprite.Sprite):
	def __init__(self, magiccake, offset, direction):
		pg.sprite.Sprite.__init__(self)
		self.MagicCake = magiccake
		self.image = pg.Surface((50, 50))
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = WIDTH/2 - offset
		self.rect.y = HEIGHT - HEIGHT/8
		self.is_active = False
		self.direction = direction

	def update(self):
		# Check for colision with coursor
		#print('PAGINATOR STATE' + str(self.is_active))
		hits = pg.sprite.collide_rect(self, self.MagicCake.mouse)
		if hits:
			self.is_active = True
		else:
			self.is_active = False

		# Change color when mouse hover
		if self.is_active:
			self.image.fill(RED)
		else:
			self.image.fill(WHITE)


class Scroller(pg.sprite.Sprite):
	def __init__(self, magiccake):
		pg.sprite.Sprite.__init__(self)
		self.MagicCake = magiccake
		self.image = pg.Surface((300, 50))
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = WIDTH/2 - 150
		self.rect.y = HEIGHT/3

		self.is_active = False
		self.item_number = 0
		self.list = []
		self.item = None
		self.is_editable = False


	def update(self):
		# Check if any ingredient is active
		for cake in self.MagicCake.all_cakes:
			if cake.is_active:
				for ingr in cake.ingredients:
					if ingr.is_active:
						self.is_active = True
						# set scroller list equal selected ingredient list
						self.list = ingr.scroll_list
						break
					else:
						# Set inactive state
						self.is_active = False
					#	self.list = []
		

		# Item number cant be greater than list length
		#if len(self.list) < self.item_number:
			#self.item_number = 0


		#print('Cake Scroll list: ' + str(self.list))
		#print('Scroll status:  ' + str(self.is_active))
		print('IS EDITABLE _________________-:  ' + str(self.is_editable))
	

	def setItemNumber(self, arrow):
		# Change ingr number to display
		if arrow == 'right':

			self.item_number += 1
			# Check if number is not greater than list length, number is used as index for item pick
			if self.item_number == len(self.list):
				self.item_number = 0
		elif arrow == 'left':
			self.item_number -= 1
			# Check if number is not negative 
			if self.item_number < 0:
				self.item_number = len(self.list) - 1




	def display_item(self):
		if self.MagicCake.current_page == 2 and self.is_active:
			if self.is_editable:
				# Input is displayed
				pass



			else:
				# Check what kinde of value is displayed from the list and build text for it
				if self.item_number == 0:
					#  Name case
					type_text = ""
					# Unit
					unit_text = ''
				if self.item_number == 1:
					#  How much case
					type_text = "Ilość: "
					# Unit
					unit_text = ' g'
				if self.item_number == 2:
					#  Prot case
					type_text = "Białko: "
					# Unit
					unit_text = ' g'
				if self.item_number == 3:
					#  Carb case
					type_text = "Węgle: "
					# Unit
					unit_text = ' g'
				if self.item_number == 4:
					#  Fat case
					type_text = "Tłuszcz: "
					# Unit
					unit_text = ' g'
				if self.item_number == 5:
					#  Kcal case
					type_text = "Kalorie: "
					# Unit
					unit_text = ' kcal'
				if self.item_number == 6:
					#  Pakage size case
					type_text = "Rozmiar opakowania: "
					# Unit
					unit_text = ' g'
				if self.item_number == 7:
					#  Price case
					type_text = "Cena: "
					# Unit
					unit_text = ' zł'

				font = pg.font.SysFont('Courier', 16, False, False)
				

				# Set text
				if self.list:
					text_to_edit = font.render("{}{}{}".format(type_text, self.list[self.item_number], unit_text), True, RED)
				else:
					text_to_edit = font.render(str("No items in the list"), True, RED)


								 
					# Render the text. "True" means anti-aliased text.
					# Black is the color. The variable BLACK was defined
					# above as a list of [0, 0, 0]
					# Note: This line creates an image of the letters,
					# but does not put it on the screen yet.

				# TEXTS TO BLIT:	
				
				
					
				self.MagicCake.screen.blit(text_to_edit, [self.rect.x + 4, self.rect.y + 15])



class Arrow(pg.sprite.Sprite):
	def __init__(self, magiccake, dir, x, y):
		pg.sprite.Sprite.__init__(self)
		self.MagicCake = magiccake
		self.dir = dir

		self.image = pg.Surface((50, 50))
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.i = 0
		self.is_active = False
		self.is_highlighted = False

	

	def update(self):
		# Check for collision with mouse to highlight arrow
		hits = pg.sprite.collide_rect(self, self.MagicCake.mouse)
		if hits:
			self.image.fill(GREEN)
			self.is_highlighted = True
		else:
			self.image.fill(RED)
			self.is_highlighted = False


	def change(self):
		if self.dir =='left':
			# Change number
			pass
		elif self.dir =='right':
			pass



class Trash(pg.sprite.Sprite):
	def __init__(self, magiccake):
		pg.sprite.Sprite.__init__(self)
		self.MagicCake = magiccake
		self.image = pg.Surface((40, 40))
		self.image.fill(VIOLET)
		self.rect = self.image.get_rect()
		self.rect.x = 680
		self.rect.y = 535

		self.is_active = False
		self.obj = None
		self.message = ''

	def update(self):
		pass



	def set_obj(self):
		# Check for active cake on page 1
		if self.MagicCake.current_page == 1:
			for cake in self.MagicCake.all_cakes:
				if cake.is_active:
					self.message = 'Czy chcesz usunac ciasto {}'.format(cake.name)
					self.obj = cake
					break
		# Check for active ingredients on page 2
		elif self.MagicCake.current_page == 2:
			for cake in self.MagicCake.all_cakes:
				for ingr in cake:
					if ingr.is_active:
						self.message = 'Czy chcesz usunac składnik {}'.format(ingr.name)
						self.obj = ingr
						break





	def kill_obj(self):
		pass

	def show_message(self, obj):
		# validate object
		if obj == None:
			return

		# Set message
		if self.MagicCake.current_page == 1:
			self.message = 'Czy chcesz skasowac {}'.format(obj.name)
			print (self.message)
		elif self.MagicCake.current_page == 2:
			print(str(obj) + ' <------------object podany do trasha')
			self.message = 'Czy chcesz skasowac {}'.format(obj.name)
			print (self.message)
		#self.obj = obj

		self.is_active = True
		if self.is_active:
			# Create message object
			msg = Message(self.MagicCake, self.message)
			# Waiting for confirmation
			answer = msg.wait()
			print('Odpowiedz: ' + str(answer))
			if answer:
				print ('OBJEKT DO SKASOWANIA: ' + str(obj))
				obj.kill()
			msg.kill()
			

class Message(pg.sprite.Sprite):
	def __init__(self, magiccake, message):
		pg.sprite.Sprite.__init__(self)
		self.MagicCake = magiccake
		self.image = pg.Surface((400, 100))
		self.image.fill(LAVENDER)
		self.rect = self.image.get_rect()
		self.rect.x = WIDTH/2 - 200
		self.rect.y = HEIGHT/2 - 100

		self.message = message

		


		# Yes rect
		self.yes = pg.Surface((50, 30))
		self.yes.fill(GREEN)
		self.yes_rect = self.yes.get_rect()
		self.yes_rect.x = WIDTH/2 - 60
		self.yes_rect.y = HEIGHT/2 - 40

		# No rect
		self.no = pg.Surface((50, 30))
		self.no.fill(RED)
		self.no_rect = self.yes.get_rect()
		self.no_rect.x = WIDTH/2 + 10
		self.no_rect.y = HEIGHT/2 - 40

		# Clocl
		self.clock = pg.time.Clock()

		

		

	def update(self):
		# Check for mous position

		self.mouse_pos = pg.mouse.get_pos()
		print('POZYCJA MYSZY : '+str(self.mouse_pos))


	
	def events(self):
		pass



	def show_text(self, message):
		font = pg.font.SysFont('Courier', 16, False, False)
		text = font.render(message, True, RED)
		self.MagicCake.screen.blit(text, [WIDTH/2, HEIGHT/2]) 


	def draw(self):
		self.image.fill(LAVENDER)
		pg.draw.rect(self.image, LAVENDER, self.rect, 2)
		#pg.draw.rect(self.image, RED, (20, 20, 30, 30), 0)
		#pg.draw.rect(self.image, RED, self.yes, 0)

		#draw self. on the main screen
		self.MagicCake.screen.blit(self.image, self.rect)
		self.MagicCake.screen.blit(self.yes, self.yes_rect)
		self.MagicCake.screen.blit(self.no, self.no_rect)
		
		# show text (message)
		font = pg.font.SysFont('Courier', 16, False, False)
		text = font.render(self.message, True, RED)
		yes_text = font.render('TAK', True, BLACK)
		no_text = font.render('NIE', True, BLACK)
		# Question text blit
		self.MagicCake.screen.blit(text, [self.rect.x + 10, self.rect.y + 10])
		# Yes and No blit
		self.MagicCake.screen.blit(yes_text, [self.yes_rect.x + 10, self.yes_rect.y + 5])
		self.MagicCake.screen.blit(no_text, [self.no_rect.x + 10, self.no_rect.y + 5])

		print('Message to display: ' + self.message)

		# show message text

		

		pg.display.update()

	def wait(self):
		self.waiting = True
		while self.waiting:
			self.clock.tick(FPS)
			print("WHILE LOOP STARTED")
			self.update()
			# update message window

			# Sprawdz eventy
			for event in pg.event.get():
				if event.type == pg.QUIT:
					self.waiting = False
					self.MagicCake.running= False
					
				# Check for keyboard for typing letters
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_n:
						self.waiting = False

				# Check for klick
				if event.type == pg.MOUSEBUTTONUP:
					# When click on Yes rect 
					if 490 < self.mouse_pos[0] < 540 and 260 < self.mouse_pos[1] < 290: 
						print('YES CLICK')
						return self.answer(1)
						#self.waiting = 
					elif 560 < self.mouse_pos[0] < 610 and 260 < self.mouse_pos[1] < 290: 
						print('NO CLICK')
						return self.answer(0)
			self.draw()
	
	
	def answer(self, answer):
		if answer == 1:
			return True
		else:
			return False
		

class List(pg.sprite.Sprite):
	'''
	Class that makes list of objects in collection, returns given amount (10) elements from collection,
	provides scrolling list ability
	'''
	def __init__(self, magiccake):
		pg.sprite.Sprite.__init__(self)
		self.MagicCake = magiccake
		#self.collection = collection
		self.start_index = 0
		self.collection_to_return = pg.sprite.Group()

		# Buttons
		self.buttons = pg.sprite.Group()
		self.button_up = None
		self.button_down = None

	

		# BUTTONS HERE
		
	#def set_scroll_butons_position(self):
		#self.rect_up.rect.x = self.items_to_displa



	def select_objects(self, collection, items_to_display=10, space=10):
		'''
		Similar to update methods, refreshed every frame
		'''
		
		# Start index setup (it cant be greater than items to display)
		# Check if index is greater than collection lenght
		if self.start_index > len(collection):
			self.start_index = len(collection) - 1

		# Check for case when there is no more items to display
		if self.start_index > 0:
			if items_to_display + self.start_index >= len(collection):
				self.start_index -= 1 
		

		elif self.start_index < 0:
			self.start_index = 0


		# Making group of 10 selected sprites ( 10 by default)
		self.collection = collection
		self.selected = []
		self.items_to_display = items_to_display
		self.space = space
		for item in self.collection:
			self.selected.append(item) 
		
		self.selected = self.selected[self.start_index : self.items_to_display + self.start_index]



		# ------------------------------------------------------------------------------DEBUG
		for i in self.selected:
			print('Lista selected do  wyswietlenia' + str(i.name))



		# Seting position of selected items
		self.set_position()

		# Update buttons
		self.buttons.update()


		
		# Setting buttons to scroll if needed (if lenght of list is greather than quantity of objects to display)
		if self.items_to_display < len(self.collection):
			if len(self.buttons) < 2:
				self.create_buttons()
		else:
			self.buttons.empty()

	

	def set_position(self):
		'''
		Seting position for each element in elements selected list of given size 
		'''
		for num, item in enumerate(self.selected):
			# Check if item is on right place
			if item.rect.y > (num + 1) * (item.rect.height + self.space) - 20:
				# if not make it move to the right place
				item.rect.y -= 9
				if item.rect.y < (num + 1) * (item.rect.height + self.space) - 20:
					item.rect.y = ((num + 1) * (item.rect.height + self.space) - 20) 

	def update_given_collection(self):
		'''
		Use this method in draw section. Method returns list of items to display.
		'''
		
		# Clearing colection
		self.collection_to_return.empty()
		# Making new collection
		for item in self.selected:
			self.collection_to_return.add(item)
			#print('item in list t return acc: ' + str(item.vel))
		return self.collection_to_return


	def set_out_of_list(self):
		'''
		Handling position of items that are out of display range. They wait in one place to be displayed)
		'''
		for num, item in enumerate(self.collection):
			# Set up one position for all objects out of display range
			if num >= self.items_to_display:
				item.rect.y = (self.space + item.rect.height) * self.items_to_display
		return self.collection


	def create_buttons(self):
		'''
		Creates buttons when list is longer then given max lenght of itself.
		'''

		# Check for position of last element
		x = 0
		y = 0

		for item in self.collection_to_return:
			x = item.rect.x
			y = item.rect.y


		# Creating Buttons for the list
		self.button_up = Button(self.MagicCake, x, y + 60, 90, 30)
		self.button_down = Button(self.MagicCake, x + 110, y + 60, 90, 30, boundry_right=WIDTH-200+90)
		self.buttons.add(self.button_up)
		self.buttons.add(self.button_down)


	def buttons_to_draw(self):
		'''
		Returns list of buttons to draw
		'''
		return self.buttons






class Button(pg.sprite.Sprite):
	'''
	Button class that handels clicking and returns True
	'''

	def __init__(self, magiccake, x, y, width, height, color=RED, sec_color=GREEN, boundry_left=-300, boundry_right=WIDTH-220):
		pg.sprite.Sprite.__init__(self)
		self.MagicCake = magiccake
		self.image = pg.Surface((width, height))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)
		self.pos = vec(x, y)
		self.boundry_left = boundry_left
		self.boundry_right = boundry_right
		

		self.color = color
		self.sec_color = sec_color

	def update(self):

		# Basic mouvment
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc

		self.rect.x = self.pos.x
		self.rect.y = self.pos.y

		# Stop it!
		# Left
		if self.pos.x <= self.boundry_left:
			self.vel = vec(0, 0)
			self.acc = vec(0, 0)
			self.pos.x = self.boundry_left + 1
			
		
		# Right
		if self.pos.x >= self.boundry_right:
			self.vel = vec(0, 0)
			self.acc = vec(0, 0)
			self.pos.x = self.boundry_right
			




		# Check for collision with mouse
		hits = pg.sprite.collide_rect(self, self.MagicCake.mouse)
		if hits:
			# Change background color
			self.image.fill(self.sec_color)
		else:
			# Set default background color
			self.image.fill(self.color)

		# próbujemy sprawdzic klikniecie
		#for event in pg.event.get():


		



		
		
