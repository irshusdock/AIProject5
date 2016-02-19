"arkessler & irshusdock"
"Alexi Kessler & Ian Shusdock"

import sys


class Item:
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight

class Bag:
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight

class Capacity_Constraint:
	def __init__(self):
		self.lower_limit = 0.9
		self.upper_limit = 1.0

class Fit_Constraint:
	def __init__(self, minimum, maximum):
		self.min = minimum
		self.max = maximum

class Unary_Inclusive_Constraint:
	def __init__(self, item_name, list_of_bag_names):
		self.item_name = item_name
		self.list_of_bag_names = list_of_bag_names

class Unary_Exclusive_Constraint:
	def __init__(self, item_name, list_of_bags):
		self.item_name = item_name
		self.list_of_bags = list_of_bags

class Binary_Equals_Constraint:
	def __init__(self, item1_name, item2_name):
		self.item1_name = item1_name
		self.item2_name = item2_name

class Binary_Not_Equals_Constraint:
	def __init__(self, item1_name, item2_name):
		self.item1_name = item1_name
		self.item2_name = item2_name

class Mutual_Inclusive_Constraint:
	def __init__(self, item1_name, item2_name, bag1_name, bag2_name):
		self.item1_name = item1_name
		self.item2_name = item2_name
		self.bag1_name = bag1_name
		self.bag2_name = bag2_name


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

	"Set the capacity constraints"
	capacity_constraints = [Capacity_Constraint()]

	fit_constraints = []

	"Add item fit constraints if there are any"
	if(file_content[0] != "#"):
		fit_constraints.append(Fit_Constraint(file_content[0][0], file_content[0][2]))
		file_content = file_content[2:]
	else:
		file_content = file_content[1:]
	
	unary_inclusive_constraints = []
	index = 0

	"Add unary inclusive constraints if any"
	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		temp = line.split(" ")
		unary_inclusive_constraints.append(Unary_Inclusive_Constraint(temp[0], temp[1:]))

	file_content = file_content[index:]

	unary_exclusive_constraints = []
	index = 0

	"Add unary exclusive constraints if any"
	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		temp = line.split(" ")
		unary_exclusive_constraints.append(Unary_Exclusive_Constraint(temp[0], temp[1:]))

	file_content = file_content[index:]

	binary_equals_constraints = []
	index = 0

	"Add binary equals constraints if any"
	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		temp = line.split(" ")
		binary_equals_constraints.append(Binary_Equals_Constraint(temp[0], temp[1]))

	file_content = file_content[index:]

	binary_not_equals_constraints = []
	index = 0

	"Add binary not equals constraints if any"
	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		temp = line.split(" ")
		binary_not_equals_constraints.append(Binary_Not_Equals_Constraint(temp[0], temp[1]))

	file_content = file_content[index:]

	mutual_inclusive_constraints = []
	index = 0

	"Add mutual inclusive constraints if any"
	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		temp = line.split(" ")
		mutual_inclusive_constraints.append(Mutual_Inclusive_Constraint(temp[0], temp[1], temp[2], temp[3]))



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
