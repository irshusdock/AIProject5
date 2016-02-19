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




"Main script for the program"
def project5_main():
	
	f = open(sys.argv[1])
	file_content = f.readlines()
	f.close()
	
	file_content = file_content[1:]

	items = []
	index = 0

	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		items.append(Item(line[0], line[2]))

	file_content = file_content[index:]

	bags = []
	index = 0

	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		bags.append(Bag(line[0], line[2]))
		



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
