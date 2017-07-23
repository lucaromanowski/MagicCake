import os


class Memory(object):
	'''
	class responsible for saving objects (cakes and ingredients)
	'''
	def __init__(self):
		pass

	def save(self, object=None, group=None):
		'''
		Method can take object or group of objects and save it to a file
		'''
		if object:
			with open('testfile.txt', 'w') as f:
				# Saving cake name
				f.write(str(object.name) + '\n')
				# Saving cake ingredients
				for ingr in object.ingredients:
					f.write(str(ingr.name) + '\n')
				f.write('end' + '\n')

		



