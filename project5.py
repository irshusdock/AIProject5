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

	"Return the bag name this constraint works on"
	def get_name(self):
		return self.name

"Class for the weight capacity constraint of bags"
"bag is the bag the constraint falls on"
"All bags must be at least 90% filled (by weight)"
"All bags must be at most 100% filled (by weight)"
class Capacity_Constraint:
	def __init__(self, bag):
		self.lower_limit = 0.9
		self.upper_limit = 1.0
		self.bag = bag

	"Check to see if the constraint holds with the given assignment"
	"assignments is the list of item-bag assignments"
	"items is the list of Item objects"
	"returns a boolean"
	def check_constraint(self, assignments, items):
		sum_weights = 0

		for assignment in assignments:
			if(assignment.get_bag() == self.bag.get_name()):
				for item in items:
					if(item.get_name() == assignment.get_name()):
						sum_weights = sum_weights + item.get_weight()
						break
		if(sum_weights * 1.0/bag.get_weight() <= 1.0):
			if(sum_weights * 1.0/bag.get_weight >= 0.9):
				return True
		return False

	"Check to see if the bag is not over the weight capacity"
	"assignments is the list of item-bag assignments"
	"items is the list of Item objects"
	"returns a boolean"
	def check_upper_limit(self, assignments, items):
		for assignment in assignments:
			if(assignment.get_bag() == self.bag.get_name()):
				for item in items:
					if(item.get_name() == assignment.get_name()):
						sum_weights = sum_weights + item.get_weight()
						break
		if(sum_weights * 1.0/bag.get_weight() <= 1.0):
			return True
		return False

	def print_out(self):
		print("Capacity constraint: bag", self.bag.get_name())

"Class for the number of items constraint of bags"
"bag is the bag the constraint falls on"
"minimum is the minimum number of items that must be in a bag"
"maximum is the maximum number of items that can be in a bag"
class Fit_Constraint:
	def __init__(self, bag, minimum, maximum):
		self.min = minimum
		self.max = maximum
		self.bag = bag

	"Check to see if the constraint holds with the given assignment"
	"assignments is the list of item-bag assignments"
	"items is the list of Item objects"
	"returns a boolean"
	def check_constraint(self, assignments, items):
		item_count = 0
		for assignment in assignments:
			if(assignment.get_bag() == self.bag.get_name()):
				item_count = item_count + 1
		if(item_count >= self.minimum):
			if(item_count <= self.maximum):
				return True
		return False

	"Check to see if the bag is not over the item limit capacity"
	"assignments is the list of item-bag assignments"
	"items is the list of Item objects"
	"returns a boolean"
	def check_upper_limit(self, assignments, items):
		item_count = 0
		for assignment in assignments:
			if(assignment.get_bag() == self.bag.get_name()):
				item_count = item_count + 1
		if(item_count <= self.maximum):
			return True
		return False

	def print_out(self):
		print("Fit Constraint: bag", self.bag.get_name(), " must have between", self.min, " and", self.max, "items")

"Class for the unary inclusive constraints of items"
"item_name is the name of the item the constraint pretains to"
"list_of_bag_names is the list of bags that the item is allowed to be placed in"
class Unary_Inclusive_Constraint:
	def __init__(self, item_name, list_of_bag_names):
		self.item_name = item_name
		self.list_of_bag_names = list_of_bag_names

	"Check to see if the constraint holds with the given assignment"
	"assignments is the list of item-bag assignments"
	"returns a boolean"
	def check_constraint(self, assignments):
		for assignment in assignments:
			if(assignment.get_name() == self.item_name):
				if(assignment.get_bag() in self.list_of_bags):
					return True
				else:
					return False

	def print_out(self):
		print("Unary Inclusive Constraint: Item", self.item_name, "must be placed in any of bags")
		for bag in self.list_of_bag_names:
			print(bag)

"Class for the unary exclusive constraints of items"
"item_name is the name of the item the constraint pretains to"
"list_of_bag_names is the list of bags that the item is NOT allowed to be placed in"
class Unary_Exclusive_Constraint:
	def __init__(self, item_name, list_of_bags):
		self.item_name = item_name
		self.list_of_bags = list_of_bags

	"Check to see if the constraint holds with the given assignment"
	"assignments is the list of item-bag assignments"
	"returns a boolean"
	def check_constraint(self, assignments):
		for assignment in assignments:
			if(assignment.get_name() == self.item_name):
				if(assignment.get_bag() in self.list_of_bags):
					return False
				else:
					return True

	def print_out(self):
		print("Unary Exclusive Constraint: Item", self.item_name, "cannot be placed in any of bags ")
		for bag in self.list_of_bags:
			print(bag)

"Class for the binary equals constraints of items"
"item1_name is the name of the first item"
"item2_name is the name of the second item"
"This constraint says item1 and item2 must be placed in the same bag"
class Binary_Equals_Constraint:
	def __init__(self, item1_name, item2_name):
		self.item1_name = item1_name
		self.item2_name = item2_name


	"Check to see if the constraint holds with the given assignment"
	"assignments is the list of item-bag assignments"
	"returns a boolean"
	def check_constraint(self, assignments):
		for assignment in assignments:
			if(assignment.get_name() == self.item1_name):
				bag1 = assignment.get_bag()
			if(assignment.get_name() == self.item2_name):
				bag2 = assignment.get_bag()

		if((bag1 == bag2) or (bag1 == "")  or (bag2 == "")):
			return True
		else:
			return False

	def print_out(self):
		print("Binary Equals Constraint: Item", self.item1_name, "must be in the same bag as", self.item2_name, end="")

"Class for the binary not equals constraints of items"
"item1_name is the name of the first item"
"item2_name is the name of the second item"
"This constraint says item1 and item2 must be placed in different bags"
class Binary_Not_Equals_Constraint:
	def __init__(self, item1_name, item2_name):
		self.item1_name = item1_name
		self.item2_name = item2_name

	"Check to see if the constraint holds with the given assignment"
	"assignments is the list of item-bag assignments"
	"returns a boolean"
	def check_constraint(self, assignments):
		for assignment in assignments:
			if(assignment.get_name() == self.item1_name):
				bag1 = assignment.get_bag()
			if(assignment.get_name() == self.item2_name):
				bag2 = assignment.get_bag()

		if((bag1 != bag2) or (bag1 == "")  or (bag2 == "")):
			return True
		else:
			return False

	def print_out(self):
		print("Binary Not Equals Constraint: Item", self.item1_name, "cannot be in the same bag as", self.item2_name, end="")

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

	"Check to see if the constraint holds with the given assignment"
	"assignments is the list of item-bag assignments"
	"returns a boolean"
	def check_constraint(self, assignments):
		for assignment in assignments:
			if(assignment.get_name() == self.item1_name):
				bag1 = assignment.get_bag()
			if(assignment.get_name() == self.item2_name):
				bag2 = assignment.get_bag()

		if(((bag1 == self.bag1_name) and (bag2 == self.bag2_name)) or ((bag1 == self.bag2_name) and (bag2 == self.bag1_name)) or (bag1 == "") or (bag2 == "")):
			return True
		else:
			return False

	def print_out(self):
		print("Mutual Inclusive Constraint: If item", self.item1_name, "is in either bag", self.bag1_name, "or bag", self.bag2_name, "then item", self.item2_name, "must be in the other bag")

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

	"Return the item_name of the assignment"
	def get_item(self):
		return this.item_name

	"Set the value of the bag to the passed value"
	"bag_name is the name of the bag to set"
	def set_bag(self, bag_name):
		this.bag_name = bag_name

"Class to hold all problem constraints"
"capacity_constraints is the list of capacity constraints"
"fit_constraints is the list of fit constraints"
"unary_inclusive_constraints is the list of unary inclusive constraints"
"unary_exclusive_constraints is the list of unary exclusive constraints"
"binary_equals_constraints is the list of binary equals constraints"
"binary_not_equals_constraints is the list of binary not equals constraints"
"mutual_inclusive_constraints is the list of mutual inclusive constraints"
class Constraint_Container:
	def __init__(self, capacity_constraints, fit_constraints, unary_inclusive_constraints, unary_exclusive_constraints, 
		binary_equals_constraints, binary_not_equals_constraints, mutual_inclusive_constraints):
		self.capacity_constraints = capacity_constraints
		self.fit_constraints = fit_constraints
		self.unary_inclusive_constraints = unary_inclusive_constraints
		self.unary_exclusive_constraints = unary_exclusive_constraints
		self.binary_equals_constraints = binary_equals_constraints
		self.binary_not_equals_constraints = binary_not_equals_constraints
		self.mutual_inclusive_constraints = mutual_inclusive_constraints
	def print_constraints(self):
		for capacity_constraint in self.capacity_constraints:
			capacity_constraint.print_out()
		for fit_constraint in self.fit_constraints:
			fit_constraint.print_out()
		for unary_inclusive_constraint in self.unary_inclusive_constraints:
			unary_inclusive_constraint.print_out()
		for unary_exclusive_constraint in self.unary_exclusive_constraints:
			unary_exclusive_constraint.print_out()
		for binary_equals_constraint in self.binary_equals_constraints:
			binary_equals_constraint.print_out()
		for binary_not_equals_constraint in self.binary_not_equals_constraints:
			binary_not_equals_constraint.print_out()

class CSP_Full:
	def __init__(self, items, bags, constraint_container):
		self.items = items
		self.bags = bags
		self.constraints = constraint_container
	
"---------------------End Class definitions, begin function definitions---------------------"

"Checks if all items have been assigned to bag"
"assignment is a list of item-bag Assignments"
"returns a boolean "
def fully_assigned(assignments):
	for assignment in assignments:
		if(assignment.get_bag() == ""):
			return False
	return True

"Return an unassigned variable name from the assignment list"
"assignments is the list of assignments of variables"
"returns a string"
def select_unassigned(assignments):
	for assignment in assignments:
		if(assignment.get_bag() == ""):
			return assignment.get_item()
	#TODO add intelligent selection of items
	#MRV
	#Degree
	#LCV


"Return the possible domain values for the given variable based on the contraints and the assignments so far"
"Only checks domain based on unary inclusive and unary exclusive constraints"
"current_variable is the name of the variable to get the domain of"
"assignments is the list of assignments of all variables so far"
"constraints is the set of combined constraints (for the entire problem)"
"returns a list"
def get_domain_values(current_variable, assignments, constraints):
	print("Constructing domain for:" . current_variable)
	domain = []

	print(domain)
	return domain

"Return whether or not assigning a particular variable and particular value given a particular assignment causes an inconsistency"
"Note: Some constraints may still not be satisfied, but it is important that contraints on variables (items) already assigned are satisfied"
"current_variable is the variable to be assigned (i.e. item)"
"value is the value to assign to that variable (i.e. bag)"
"assignments is the list of current item-bag assignments"
"constraints is the set of combined contraints (for the entire problem)"
"returns a boolean"
def consistent_with_constraints(current_variable, value, assignments, constraints):
	for assignment in assignment:
		if (assignment.get_name() == current_variable):
			assignment.value = value
			if (satisfies_constraints(assignments, constraints)):
				return True
			else:
				assignment.value = ""
				return False
	return False

"Returns the passed list of assignments after updating the assignment of the passed variable"
"assignments is the current list of item-bag assignments to update"
"current_variable is the variable (item) to update"
"value is the value (bag) to assign to the variable (item)"
"returns a list of assignments"
def update_assignments(assignments, current_variable, value):
	for assignment in assignments:
		if(assignment.get_name() == current_variable):
			assignment.set_bag(value)
			return

"Checks if the given variable assignments satisfy all problem constraints"
"assignments is the list of item-bag assignments"
"constraints is the set of combined constraints (for the entire problem)"
"returns a boolean"
def satisfies_constraints(assignments, constraints):
	for capacity_constraint in constraints.capacity_constraints:
		if (capacity_constraint.check_constraint() == False):
			return False
	for fit_constraint in constraints.fit_constraints:
		if (fit_constraint.check_constraint() == False):
			return False
	for unary_inclusive_constraint in constraints.unary_inclusive_constraints:
		if (unary_inclusive_constraint.check_constraint() == False):
			return False
	for unary_exclusive_constraint in constraints.unary_exclusive_constraints:
		if (unary_exclusive_constraint.check_constraint() == False):
			return False
	for binary_equals_constraint in constraints.binary_equals_constraints:
		if (binary_equals_constraint.check_constraint() == False):
			return False
	for binary_not_equals_constraint in constraints.binary_not_equals_constraints:
		if (binary_not_equals_constraint.check_constraint() == False):
			return False
	for mutual_inclusive_constraint in constraints.mutual_inclusive_constraints:
		if (mutual_inclusive_constraint.check_constraint() == False):
			return False
	return True

"Run backtrack search on the passed assignment and constraints"
"assignments is the list of item-bag assignments"
"constraints is the set of combined constraints (for the entire problem)"
"returns \"failure\" if there is no possible solution with the given assignments"
"returns a list of assignments if that list satisfies all problem constraints"
def backtrack(assignments, constraints):

	"If every variable has been assigned, check that the assignment satisfies all constraints. If the assignment does, return it"
	if(fully_assigned(assignments)):
		if(satisfies_constraints(assignments, constraints)):
			return assignments

	"Choose an unassigned variable"
	current_variable = select_unassigned(assignments)

	"Check every possible value that variable can take. If no value leads to a solution, there is no solution for the given assignment"
	for value in get_domain_values(current_variable, assignments, constraints):

		"Check if the value chosen is consistent with the rest of the assignments so far"
		if (consistent_with_constraints(current_variable, value, assignments, constraints)):	

			"If it is consistent, assign the variable that value to run backtrack using the new assignment"
			assignments = update_assignments(assignments, current_variable, value)
			result = backtrack(assignments, constraints)
			
			"If backtrack returns an assignment, we have found a solution so cascade up"
			if(result != "failure"):
				return result

			"Otherwise remove that item-bag assignment"
			assignments.update_assignments(assignments, current_variable, "")
		

	"Return failure if all possible values have been checked. There is no solution for the given assignment"
	return "failure"

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
			//Everything involving the inferences is apparently optional
			inferences = inferene(CSP, current_variable, value)
			if (inferences != failure) 
			{
				assignment.add(inferences)
				result = backtrack(assignment, CSP)
				if (result != failure)
					return result
			}
		}
		else
		{
			remove assigned value and inferences
		}
}

'''

"Main script for the program"
def project5_main():
	
	items = []
	bags = []
	assignments = []

	capacity_constraints = []
	fit_constraints = []
	unary_inclusive_constraints = []
	unary_exclusive_constraints = []
	binary_equals_constraints = []
	binary_not_equals_constraints = []
	mutual_inclusive_constraints = []

	constraint_container = Constraint_Container(capacity_constraints, fit_constraints, unary_inclusive_constraints, unary_exclusive_constraints, 
		binary_equals_constraints, binary_not_equals_constraints, mutual_inclusive_constraints)

	CSP = CSP_Full(items, bags, constraint_container)

	"Check for proper number of arguments"
	if (len(sys.argv) < 2):
		#TODO fill in proper usage
		print("Usage is py project5.py ... ... ...")
		sys.exit()

	f = open(sys.argv[1])
	file_content = f.readlines()
	f.close()
	
	file_content = file_content[1:]

	index = 0

	"Parse the Items"
	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		items.append(Item(line[0], line[2]))

	"Update CSP"
	CSP.items = items
	"Reset file_content and index"
	file_content = file_content[index:]
	index = 0

	"Parse the Bags"
	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		bags.append(Bag(line[0], line[2]))
		
	"Update CSP"
	CSP.bags = bags
	"Reset file_content and index"
	file_content = file_content[index:]
	index = 0

	"Set the capacity constraints"
	for bag in bags:
		capacity_constraints.append(Capacity_Constraint(bag))

	"Update constraint_container"
	constraint_container.capacity_constraints = capacity_constraints

	"Add item fit constraints if there are any"
	if(file_content[0] != "#"):
		for bag in bags:
			fit_constraints.append(Fit_Constraint(bag, file_content[0][0], file_content[0][2]))
		file_content = file_content[2:]
	else:
		file_content = file_content[1:]
	
	"Update constraint_container"
	constraint_container.fit_constraints = fit_constraints
	"Reset index"
	index = 0

	"Add unary inclusive constraints if any"
	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		temp = line.split(" ")
		unary_inclusive_constraints.append(Unary_Inclusive_Constraint(temp[0], temp[1:]))

	"Update constraint_container"
	constraint_container.unary_inclusive_constraints = unary_inclusive_constraints
	"Reset file_content and index"
	file_content = file_content[index:]
	index = 0

	"Add unary exclusive constraints if any"
	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		temp = line.split(" ")
		unary_exclusive_constraints.append(Unary_Exclusive_Constraint(temp[0], temp[1:]))

	"Update constraint_container"
	constraint_container.unary_exclusive_constraints = unary_exclusive_constraints
	"Reset file_content and index"
	file_content = file_content[index:]
	index = 0

	"Add binary equals constraints if any"
	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		temp = line.split(" ")
		binary_equals_constraints.append(Binary_Equals_Constraint(temp[0], temp[1]))

	"Update constraint_container"
	constraint_container.binary_equals_constraints = binary_equals_constraints
	"Reset file_content and index"
	file_content = file_content[index:]
	index = 0

	"Add binary not equals constraints if any"
	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		temp = line.split(" ")
		binary_not_equals_constraints.append(Binary_Not_Equals_Constraint(temp[0], temp[1]))

	"Update constraint_container"
	constraint_container.binary_not_equals_constraints = binary_not_equals_constraints
	"Reset file_content and index"
	file_content = file_content[index:]
	index = 0

	"Add mutual inclusive constraints if any"
	for line in file_content:
		index = index + 1
		if(line[0] == "#"):
			break
		temp = line.split(" ")
		mutual_inclusive_constraints.append(Mutual_Inclusive_Constraint(temp[0], temp[1], temp[2], temp[3]))

	constraint_container.print_constraints()

	"Update container"
	CSP.constraint_container = constraint_container

	"Create a list of assignments, assigning each variable to start without a bag"
	for item in items:
		new_assignment = Assignment(item.name, '')
		assignments.append(new_assignment)

	#TODO
	"Run backtrace using the blank assignments and the set of contraints"

	"Handle output"

	#End TODO

if __name__ == '__main__':
	project5_main()		

