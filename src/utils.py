import pygame as pg
import random

from settings import *
from sprites import *

vec = pg.math.Vector2


'''
Checking for all events in main loop
1. Quit event
2. Letter typing events
'''
def check_for_events(magiccake):
	# Check for active objects (used later to delete them in Trash class)
	active_object = None
	if magiccake.current_page == 1:
		for cake in magiccake.all_cakes:
			if cake.is_active:
				active_object = cake
				break
	elif magiccake.current_page == 2:
		for cake in magiccake.all_cakes:
			if cake.is_active:
				for ingr in cake.ingredients:
					if ingr.is_active:
						active_object = ingr
						break

	for event in pg.event.get():
			if event.type == pg.QUIT:
				magiccake.running= False
				
			# Check for keyboard for typing letters
			if event.type == pg.KEYDOWN:
				# Checking if the name is not to long
				if not len(magiccake.input.input_list) > 35:
					# Checking if youa are on a main page
					if magiccake.current_page == 1 or magiccake.scroller.is_editable:
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

						# Behavior for page 2 (editing ingredient properties)
					elif magiccake.current_page == 2:
						if magiccake.scroller.is_editable:
							print('SCROLLER DATA UPDATED')
							# Put input data to scroller list (update ingredient data)
							# Ingredient name case
							# What item we are going to edit?
							# We are editing name:
							if magiccake.scroller.item_number == 0:
								# Check wich ingredient is active
								for cake in magiccake.all_cakes:
									for ingr in cake.ingredients:
										if ingr.is_active:
											# seting up new name for an active ingredient
											ingr.name = magiccake.input.input_str
							# We are editing how much:
							elif magiccake.scroller.item_number == 1:
								try:
									# Check wich ingredient is active
									for cake in magiccake.all_cakes:
										for ingr in cake.ingredients:
											if ingr.is_active:
												# seting up new quantity for an active ingredient
												ingr.how_much = int(magiccake.input.input_str)
								except ValueError:
									pass

							# We are editing protein:
							elif magiccake.scroller.item_number == 2:
								try:
									# Check wich ingredient is active
									for cake in magiccake.all_cakes:
										for ingr in cake.ingredients:
											if ingr.is_active:
												# seting up new quantity for an active ingredient
												ingr.protein = int(magiccake.input.input_str)
								except ValueError:
									pass

							# We are editing carb:
							elif magiccake.scroller.item_number == 3:
								try:
									# Check wich ingredient is active
									for cake in magiccake.all_cakes:
										for ingr in cake.ingredients:
											if ingr.is_active:
												# seting up new quantity for an active ingredient
												ingr.carb = int(magiccake.input.input_str)
								except ValueError:
									pass

							# We are editing fat:
							elif magiccake.scroller.item_number == 4:
								try:
									# Check wich ingredient is active
									for cake in magiccake.all_cakes:
										for ingr in cake.ingredients:
											if ingr.is_active:
												# seting up new quantity for an active ingredient
												ingr.fat = int(magiccake.input.input_str)
								except ValueError:
									pass

							# We are editing kcal:
							elif magiccake.scroller.item_number == 5:
								try:
									# Check wich ingredient is active
									for cake in magiccake.all_cakes:
										for ingr in cake.ingredients:
											if ingr.is_active:
												# seting up new quantity for an active ingredient
												ingr.kcal = int(magiccake.input.input_str)
								except ValueError:
									pass

							# We are editing price:
							elif magiccake.scroller.item_number == 6:
								try:
									# Check wich ingredient is active
									for cake in magiccake.all_cakes:
										for ingr in cake.ingredients:
											if ingr.is_active:
												# seting up new quantity for an active ingredient
												ingr.package_size = int(magiccake.input.input_str)
								except ValueError:
									pass

							# We are editing price:
							elif magiccake.scroller.item_number == 7:
								try:
									# Check wich ingredient is active
									for cake in magiccake.all_cakes:
										for ingr in cake.ingredients:
											if ingr.is_active:
												# seting up new quantity for an active ingredient
												ingr.price = float(magiccake.input.input_str)
								except ValueError:
									pass


							# Clear input
							magiccake.input.input_list = []
							# deactivate scroller input
							magiccake.scroller.is_editable = False



						#DEBUG-----------------------------------------------------------------------------------------DEBUG
						#print("CAKE MADE")
			
			# Check for mouse clicking
			if event.type == pg.MOUSEBUTTONUP:
				
				# Checks for klicking on Paginator objects
				for pag in magiccake.paginators:
					if pag.is_active:
						if pag.direction == 'right':
							# Move cakes objects to the right
							for cake in magiccake.all_cakes:
								cake.is_moving = True
								cake.acc += vec(random.randrange(8, 10), 0)
								magiccake.cakegeneral.acc += vec(random.randrange(8, 10), 0)
								magiccake.current_page = 1
								# moving ingredients of cake
								for ingr in cake.ingredients:
									ingr.move('right')

							# Move cake buttons right
							for button in magiccake.list.buttons:
								button.acc += vec(random.randrange(8, 10), 0)

							# Move ingredients button right
							for button in magiccake.ingredients_collection.buttons:
								button.acc += vec(random.randrange(8, 10), 0)

							

						if pag.direction == 'left':
							# Move objects to the right
							for cake in magiccake.all_cakes:
								cake.is_moving = True
								cake.acc -= vec(random.randrange(8, 10), 0)
								magiccake.cakegeneral.acc -= vec(random.randrange(8, 10), 0)
								magiccake.current_page = 2
								# moving ingredients of cake
								for ingr in cake.ingredients:
									ingr.move('left')

							# Move cake buttons left
							for button in magiccake.list.buttons:
								button.acc -= vec(random.randrange(8, 10), 0)

							# Move ingredients button left
							for button in magiccake.ingredients_collection.buttons:
								button.acc -= vec(random.randrange(8, 10), 0)


				# Checks for klicking on cake object
				hits = pg.sprite.spritecollide(magiccake.mouse, magiccake.all_cakes, False)
				if hits:
					# Setting all cakes inactive (onlu one cake can be active at a time)
					# Paginator must be on page 1
					if magiccake.current_page == 1: 
						for cake_active in magiccake.all_cakes:
							cake_active.is_active = False
						# Setting selected cake active
						for cake in hits:
							cake.is_active = True
				else:
					if magiccake.current_page == 1:
						# When click not on cake, deselect all cakes
						for cake in magiccake.all_cakes:
							if not cake.is_moving:
								cake.is_active = False

				# Check for ckicking on Ingredient object 
				# Check for clicking on arrows of scroller (to change displayed item)
				# Check for clicking on scroller (click make edit possible)
				for cake in magiccake.all_cakes:
					if cake.is_active:
						# Czeck for klicking on ingredient
						ingr_hits = pg.sprite.spritecollide(magiccake.mouse, cake.ingredients, False)
						# Check for clicking on one of the arrows for scroller
						arrow_hits = pg.sprite.spritecollide(magiccake.mouse, magiccake.arrows, False)
						# Check for scroller clicks
						scroller_hits = pg.sprite.collide_rect(magiccake.mouse, magiccake.scroller)
						if ingr_hits:
							# Deactivate all ingredients
							for ingr in cake.ingredients:
								ingr.is_active = False
							# Activate ingr on mouse click
							for ingr in ingr_hits:
								ingr.is_active = True
						elif arrow_hits:
							# Check witch arrow was klicked (left or right)
							if arrow_hits[0].dir == 'right':
								magiccake.scroller.setItemNumber('right')
							elif arrow_hits[0].dir == 'left':
								magiccake.scroller.setItemNumber('left')
						elif scroller_hits:
							# Set editable to true (input shoud appear)
							if not magiccake.scroller.is_editable:
								magiccake.scroller.is_editable = True

						else:
							# Clicking elswear

							# deselecting scroller editable first
							if magiccake.scroller.is_editable:
								magiccake.scroller.is_editable = False
							# Deselect ingredient whille clicking elswear
							else:
								for ingr in cake.ingredients:
									ingr.is_active = False
							
				# Check for clicking on Trash object
				# Check for active objects
				trash_hits = pg.sprite.collide_rect(magiccake.mouse, magiccake.trash)
				if trash_hits:
					magiccake.trash.show_message(active_object)
					print('CLICK ON TRASH')

				# Clicking on buttons in List of cakes (not all_cakes list)
				# Checking for mouse collide with button
				button_hits = pg.sprite.spritecollide(magiccake.mouse, magiccake.list.buttons, False)
				if button_hits:
					# Bad way
					if button_hits[0] == magiccake.list.button_up:
						# Increasing sttart index ob object in collection
						magiccake.list.start_index += 1
					elif button_hits[0] == magiccake.list.button_down:
						magiccake.list.start_index -= 1

				# Checking for mouse colliding with buttons on page 2 (ingredients case)
				button_hits2 = pg.sprite.spritecollide(magiccake.mouse, magiccake.ingredients_collection.buttons, False)
				if button_hits2:
					# Bad way
					if button_hits2[0] == magiccake.ingredients_collection.button_up:
						# Increasing sttart index ob object in collection
						magiccake.ingredients_collection.start_index += 1
					elif button_hits2[0] == magiccake.ingredients_collection.button_down:
						magiccake.ingredients_collection.start_index -= 1



				

				# Check for clicking on one of the arrows for scroller
				#arrow_hits = pg.sprite.spritecollide(magiccake.mouse, magiccake.arrows, False)



# Draw text of an input on a screen
def draw_input_text(magiccake,
					surface, 
					text, 
					x, 
					y, 
					color, 
					size, 
					coursor='|', 
					is_bald=False, 
					font_name='Courier', 
					is_italic=False, 
					is_aa=True,):
	# Input displayed only on main page
#if magiccake.current_page == 1:
	# Set up for input hints
	hint1 = 'Wpisz nazwe ciasta'
	hint2 = 'Wpisz nazwe kolejnego ciasta'
	hint3 = 'Wpisz nazwe skladnika'
	hint4 = 'Wpisz nazwe kolejnego skladnika'
	hint5 = 'Podaj nową wartość'
	COL = color
	text = text
	# Hint before entering first cake name
	if len(magiccake.input.input_list) == 0:
		text = hint1
		COL = HINT_COLOR
		is_italic = True
		size = 18
	# Hint before entering another cake name
	if len(magiccake.input.input_list) == 0 and len(magiccake.all_cakes) > 0:
		text = hint2
		COL = HINT_COLOR
		is_italic = True
		size = 18
	# Hint for adding ingredient
	for cake in magiccake.all_cakes:
		if cake.is_active and len(magiccake.input.input_list) == 0:
			text = hint3
	# Hint for adding another ingredient
	for cake in magiccake.all_cakes:
		if cake.is_active and len(magiccake.input.input_list) == 0:
			if len(cake.ingredients) > 0:
				text = hint4
	# When you edit ingredient property on page 2
	if magiccake.current_page == 2 and len(magiccake.input.input_list) == 0 :
		text = hint5
		COL = HINT_COLOR
		is_italic = True
		size = 18


			
	# Blinking coursor
	# Select the font to use, size, bold, italics
	font1 = pg.font.SysFont(font_name, size, is_bald, is_italic)
	
	# Render the text. "True" means anti-aliased text.
	# Black is the color. The variable BLACK was defined
	# above as a list of [0, 0, 0]
	# Note: This line creates an image of the letters,
	# but does not put it on the screen yet.
	text = font1.render(text + coursor, is_aa, COL)
	 
	# Put the image of the text on the screen at 250x250
	surface.blit(text, [x, y])
	


