"arkessler & irshusdock"
"Alexi Kessler & Ian Shusdock"

import sys


class Item:
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
		self.bag = ""
		self.inclusive_bags = []
		self.exclusive_bags = []

	def add_inclusive_bags(self, list_of_bags):
		self.inclusive_bags = list_of_bags

	def add_exclusive_bags(self, list_of_bags):
		self.exclusive_bags = list_of_bags

	def set_bag(self, bag):
		self.bag = bag

	def get_bag(self):
		return self.bag

	def get_name(self):
		return self.name

	def get_weight(self):
		return self.weight

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
		file_content = file_content[2:]
	else:
		file_content = file_content[1:]

	index = 0

	"Add unary inclusive constraints if any"
	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		temp = line.split(" ")
		for item in items:
			if (item.get_name() == temp[0]):
				item.add_inclusive_bags(temp[1:])
				break


	"Add unary exclusive constraints if any"
	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		temp = line.split(" ")
		for item in items:
			if (item.get_name() == temp[0]):
				item.add_exclusive_bags(temp[1:])
				break

	"Add binary equals constraints if any"

	"Add binary not equals constraints if any"

	"Add mutual inclusive constraints if any"




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
