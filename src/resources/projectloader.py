'''
Loading project
'''

import os
import pickle

from settings import *


class ProjectLoader(object):
	'''
	This class loads saved projects from file and converts it to proper cake and ingredients objects.
	'''

	def __init__(self, program):
		self.program = program
		self.all_projects = []
		print('ProjectLoader Created')



	def load_all_projects(self, path=None):
		'''
		This method loads all projects. The path to the folder with projects can be specified 
		by passing the path argument. If not, method will use default path.
		'''
		print('load_all_projects ivoked')
		if not path:
			path = os.path.dirname(os.path.abspath(__file__))+SAVE_FOLDER
		print('path: ', str(path))

		# Get project folders
		walk = os.walk(path)
		for w in walk:

			print(str(w))


		