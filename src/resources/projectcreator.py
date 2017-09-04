'''
Creating project
'''
from .project import NewProject

class ProjectCreator(object):
	'''
	Class that creates new project
	'''

	def __init__(self):
		pass


	def create_project(self, name):
		return NewProject(name)