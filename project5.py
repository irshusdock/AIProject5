"arkessler & irshusdock"
"Alexi Kessler & Ian Shusdock"

import sys


"Class for an item. All items have a name and a weight"
"name is the name of the item"
"weight is how much the item weighs"
class Item:
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight

"Class for a bag. All bags have a name and a weight"
"name is the name of the bag"
"weight is how much weight the bag can hold"
class Bag:
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight

"Class for the weight capacity constraint of bags"
"All bags must be at least 90% filled (by weight)"
"All bags must be at most 100% filled (by weight)"
class Capacity_Constraint:
	def __init__(self):
		self.lower_limit = 0.9
		self.upper_limit = 1.0

"Class for the number of items constraint of bags"
"minimum is the minimum number of items that must be in a bag"
"maximum is the maximum number of items that can be in a bag"
class Fit_Constraint:
	def __init__(self, minimum, maximum):
		self.min = minimum
		self.max = maximum

"Class for the unary inclusive constraints of items"
"item_name is the name of the item the constraint pretains to"
"list_of_bag_names is the list of bags that the item is allowed to be placed in"
class Unary_Inclusive_Constraint:
	def __init__(self, item_name, list_of_bag_names):
		self.item_name = item_name
		self.list_of_bag_names = list_of_bag_names

"Class for the unary exclusive constraints of items"
"item_name is the name of the item the constraint pretains to"
"list_of_bag_names is the list of bags that the item is NOT allowed to be placed in"
class Unary_Exclusive_Constraint:
	def __init__(self, item_name, list_of_bags):
		self.item_name = item_name
		self.list_of_bags = list_of_bags

"Class for the binary equals constraints of items"
"item1_name is the name of the first item"
"item2_name is the name of the second item"
"This constraint says item1 and item2 must be placed in the same bag"
class Binary_Equals_Constraint:
	def __init__(self, item1_name, item2_name):
		self.item1_name = item1_name
		self.item2_name = item2_name

"Class for the binary not equals constraints of items"
"item1_name is the name of the first item"
"item2_name is the name of the second item"
"This constraint says item1 and item2 must be placed in different bags"
class Binary_Not_Equals_Constraint:
	def __init__(self, item1_name, item2_name):
		self.item1_name = item1_name
		self.item2_name = item2_name

"Class for the mutual inclusive constraints"
"item1_name is the name of the first item"
"item2_name is the name of the second item"
"bag1_name is the name of the first bag"
"bag2_name is the name of the second bag"
"This constraint says that if item1 is placed in bag1 or bag2, item2 must be placed in the other bag. Similarly for choosing item2 first"
class Mutual_Inclusive_Constraint:
	def __init__(self, item1_name, item2_name, bag1_name, bag2_name):
		self.item1_name = item1_name
		self.item2_name = item2_name
		self.bag1_name = bag1_name
		self.bag2_name = bag2_name

"Class to represent the assignment of an item to a bag"
"item_name is the name of the item to store"
"bag_name is the name of the bag to store the item in"
"An instance of this class states that we are storing item_name in bag_name"
"If bag_name is the empty string, that means the item has yet to be assigned"
class Assignment:
	def __init__(self, item_name, bag_name):
		self.item_name = item_name
		self.bag_name = bag_name

	"Return the bag_name of the assignment"
	def get_bag(self):
		return this.bag_name
	
	
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

"Checks if all items have been assigned to bags"
"assignment is a list of item-bag Assignments"
def fully_assigned(assignments):
	for assignment in assignments:
		if(assignment.get_bag() == ""):
			return False
	return True

"Return an unassigned variable name from the assignment list"
"assignments is the list of assignments of variables"
def select_unassigned(assignments):
	for assignment in assignments:
		if()

def backtrack(assignments, constraints):
	if(fully_assigned(assignments)):
		return assignments
	current_variable = select_unassigned(assignments)


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

