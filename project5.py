"arkessler & irshusdock"
"Alexi Kessler & Ian Shusdock"

import sys


class Item:
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight

	def set_bag(self, bag):
		self.bag = bag

	def get_bag(self):
		return self.bag

class Bag:
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
		self.items = []
	
	def add_item(self, item):
		items.append(item)

	def remove_item(self, item):
		if(item in items):
			items.remove(item)

	def add_fit_limit(self, min, max):
		self.min_items = min
		self.max_items = max


"Main script for the program"
def project5_main():
	
	f = open(sys.argv[1])
	file_content = f.readlines()
	f.close()
	
	file_content = file_content[1:]

	items = []
	index = 0

	"Parse the Items"
	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		items.append(Item(line[0], line[2]))

	file_content = file_content[index:]

	bags = []
	index = 0

	"Parse the Bags"
	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		bags.append(Bag(line[0], line[2]))
		
	file_content = file_content[index:]

	"Add item fit constraints if there are any"
	if(file_content[0] != "#"):
		for bag in bags:
			bag.add_fit_limit(file_content[0][0], file_content[0][2])
		file_content = file_content[1:]
	else:
		file_content = file_content[0:]

	index = 0

if __name__ == '__main__':
	project5_main()		
	
	
'''
Pseudo code for the backtracking algorithm

def backtrack( assignment, CSP)
{
	if (assignment is fully assigned)
		return assignment
	current_variable = select_unassigned (assignment)

	for each value in order_domain_values (current_variable, assignment, CSP )
		if value consistent with assignment 
		{
			assignment.add(current_variable = value)
			inferences = inferene(CSP, current_variable, value)
			if (inferences != failure) 
			{
				assignment.add(inferences)
				result = backtrack(assignment, CSP)
				if (result != failure)
					return result
			}
		}
}

'''
