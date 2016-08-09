""" The listdir command"""

from .base import Base

import os , sys

from pprint import pprint 

class list(Base):
    """ List the different list present in a particular parent path"""
    
    def run(self):

        def levenshtein_distance(first,second):
    
            columns = len(first) + 1
            rows = len(second) + 1
            
            current_row = [0]
             
            for column in xrange(1,columns):
                current_row.append( current_row[column - 1] + 1 ) 
                  
            for row in xrange(1,rows):
                previous_row = current_row
                current_row = [previous_row[0] + 1] 
            
                for column in xrange(1,columns):
                    top_box = previous_row[column]
                    left_box = current_row[column - 1]
                    diagonal = previous_row[column - 1]
                   
                    if first[column - 1] != second[row - 1]:
                        current_row.append(min(top_box,left_box,diagonal) +1) 
                    else: 
                        current_row.append(diagonal) 
                                
            return current_row[-1]

        def fuzzymatch(input_search, gallery):
                
                dictionary = {}

                for column in gallery:
                        search = input_search.lower()
                        library = column.lower()

                        search_index = 0
                        lib_index = 1

                        distance_list = []
                        edit_distance = 0
                        sorting_distance = edit_distance

                        for letter in library:

                                
                                if lib_index >= len(library) and search_index == len(search) - 1 and library[len(library)-1] == search[len(search) -1]:
                                        distance_list.append(library.index(letter))
         
                                        sorting_distance += (float(distance_list[-1] - distance_list[0])/(len(search)-1))

                                        first_word = search
                                        second_word = library[min(distance_list) : max(distance_list) + 1]
                                        edit_distance += levenshtein_distance(first_word,second_word)
                                        
                                        sorting_distance += 3*edit_distance

                                        
                                        if dictionary.get(sorting_distance) != None :
                                            dictionary[sorting_distance].append(library)
                                        else:
                                            dictionary[sorting_distance] = [library]
                                        break

                                if search_index == len(search):

                                        sorting_distance += (float(distance_list[-1] - distance_list[0])/(len(search)-1))

                                        first_word = search
                                        second_word = library[min(distance_list) : max(distance_list) + 1]
                                        edit_distance += levenshtein_distance(first_word,second_word)
                                        
                                        sorting_distance += 3*edit_distance
         
                                        if dictionary.get(sorting_distance) != None :
                                            dictionary[sorting_distance].append(library)
                                        else:
                                            dictionary[sorting_distance] = [library]
                                        break

                                if lib_index >= len(library):
                                    break

                                
                                if letter == search[search_index]:
                                        distance_list.append(library.index(letter))

                                        search_index += 1
                                        lib_index += 1
                                else:
                                    lib_index += 1
                

                second_list =[]
                for key in sorted(dictionary):
                    second_list.append(dictionary[key])
                return second_list[0][0]
        
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