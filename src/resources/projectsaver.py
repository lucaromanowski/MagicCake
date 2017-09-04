'''
Saving project
'''

import os
import pickle

from settings import *


class ProjectSaver(object):
	'''
	This class saves project to a file
	'''

	def __init__(self, program):
		self.program = program
		self.source_project = self.program.current_project

		
	def save(self):
		'''
		This method saves project objects to the files.
		'''

		# Create save folder if needen
		self.ensure_dir(SAVE_FOLDER)
		

	def ensure_dir(self, directory):
		'''
		This method checks if there is a directory, if not, it creates it.
		'''

		try:
			# Setting up a path for directory
			path = os.path.dirname(os.path.abspath(__file__))
			path = path + SAVE_FOLDER

			# Making directory
			os.makedirs(path)
		except:
			print('directory already exists')


	def parse_cakes(self):
		pass 

