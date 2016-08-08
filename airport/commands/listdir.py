""" The listdir command"""

from .base import Base

import os , sys

from pprint import pprint 

class list(Base):
	""" List the different list present in a particular parent path"""

	
	def run(self):

		def unix_find(pathin):
 			
 			#Return results similar to the Unix find command run without options
    		#i.e. traverse a directory tree and return all the file paths

    			return [os.path.join(path, dir)
            		for (path, dirs, files) in os.walk(pathin)
            		for dir in dirs]

		pathlist = unix_find('/users') #The parent pathway that you want to find list in 

		list = []

		#Splits the obtained list into a list 
		for line in pathlist:
			x = line.split(",")
			list.append(x)
		
		#print the index from the list
		pprint(list[0])