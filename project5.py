"arkessler & irshusdock"
"Alexi Kessler & Ian Shusdock"

import sys
global DEBUG
DEBUG = False

"Class for an item. All items have a name and a weight"
"name is the name of the item"
"weight is how much the item weighs"
class Item:
	def __init__(self, name, weight):
		self.name = name
		self.weight = float(weight)
		self.bag = ""
		self.domain = []

"Class for a bag. All bags have a name and a weight"
"name is the name of the bag"
"weight is how much weight the bag can hold"
class Bag:
	def __init__(self, name, weight):
		self.name = name
		self.weight = float(weight)

	"Return the bag name this constraint works on"
	def get_name(self):
		return self.name

"Class for the weight capacity constraint of bags"
"bag is the bag the constraint falls on"
"All bags must be at least 0% filled (by weight)"
"All bags must be at most 100% filled (by weight)"
class Capacity_Constraint:
	def __init__(self, bag):
		self.lower_limit = 0.0
		self.upper_limit = 1.0
		self.bag = bag

	"Check to see if the constraint holds with the given assignment"
	"assignments is the list of item-bag assignments"
	"items is the list of Item objects"
	"returns a boolean"
	def check_constraint(self, assignments, items):
		sum_weights = 0

		for assignment in assignments:
			if (assignment.bag != None):
				if(assignment.get_bag().get_name() == self.bag.get_name()):
					for item in items:
						if(item.name == assignment.item.name):
							sum_weights = sum_weights + item.weight
							break
		if(sum_weights/self.bag.weight <= 1.0):
			return True
		if (DEBUG):
				print("Capacity check constraint failed with ratio", sum_weights/self.bag.weight)
		return False

	"Check to see if the bag is not over the weight capacity"
	"assignments is the list of item-bag assignments"
	"items is the list of Item objects"
	"returns a boolean"
	def check_upper_limit(self, assignments, items):
		sum_weights = 0

		for assignment in assignments:
			if (assignment.get_bag() != None):
				if(assignment.get_bag().get_name() == self.bag.get_name()):
					for item in items:
						if(item.name == assignment.item.name):
							sum_weights = sum_weights + item.weight
							break
		if(sum_weights/self.bag.weight <= 1.0):
			return True
		if (DEBUG):
				print("Capacity check upper limit failed with ratio", sum_weights/self.bag.weight)
		return False

	def print_out(self):
		print("Capacity constraint: bag", self.bag.get_name())

"Class for the number of items constraint of bags"
"bag is the bag the constraint falls on"
"minimum is the minimum number of items that must be in a bag"
"maximum is the maximum number of items that can be in a bag"
class Fit_Constraint:
	def __init__(self, bag, minimum, maximum):
		self.min = int(minimum)
		self.max = int(maximum)
		self.bag = bag

	"Check to see if the constraint holds with the given assignment"
	"assignments is the list of item-bag assignments"
	"items is the list of Item objects"
	"returns a boolean"
	def check_constraint(self, assignments, items):
		item_count = 0
		for assignment in assignments:
			if (assignment.bag != None):
				if(assignment.get_bag().get_name() == self.bag.get_name()):
					item_count = item_count + 1
		if(item_count >= self.min):
			if(item_count <= self.max):
				if (DEBUG):
					print("Passed fit constraint with item_count", item_count, "with max:", self.max)
				return True
		return False

	"Check to see if the bag is not over the item limit capacity"
	"assignments is the list of item-bag assignments"
	"items is the list of Item objects"
	"returns a boolean"
	def check_upper_limit(self, assignments, items):
		item_count = 0
		for assignment in assignments:
			if(assignment.bag != None):
				if(assignment.get_bag().get_name() == self.bag.get_name()):
					item_count = item_count + 1
		if(item_count <= self.max):
			if (DEBUG):
				print("Passed fit constraint with item_count", item_count, "with max:", self.max)
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
			if(assignment.get_item().name == self.item_name):
				if(assignment.bag.name in self.list_of_bag_names):
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
			if(assignment.item.name == self.item_name):
				if(assignment.get_bag().get_name() in self.list_of_bags):
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
			if(assignment.item.name == self.item1_name):
				bag1 = assignment.get_bag()
			if(assignment.item.name == self.item2_name):
				bag2 = assignment.get_bag()

		if((bag1.name == bag2.name) or (bag1.name == "")  or (bag2.name == "")):
			return True
		else:
			return False

	def print_out(self):
		print("Binary Equals Constraint: Item", self.item1_name, "must be in the same bag as", self.item2_name, end='')

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
			if(assignment.item.name == self.item1_name):
				bag1 = assignment.get_bag()
			if(assignment.item.name == self.item2_name):
				bag2 = assignment.get_bag()

		if((bag1.name != bag2.name) or (bag1 == "")  or (bag2 == "")):
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
			if(assignment.item.name == self.item1_name):
				bag1 = assignment.get_bag()
			if(assignment.item.name == self.item2_name):
				bag2 = assignment.get_bag()

		if((bag1.name == self.bag1_name) and (bag2.name != self.bag2_name)):
			if (DEBUG):
				print("Failed mutual inclusive constraint")
				self.print_out()
			return False
		if((bag1.name == self.bag2_name) and (bag2.name != self.bag1_name)):
			if (DEBUG):
				print("Failed mutual inclusive constraint")
				self.print_out()
			return False
		if((bag2.name == self.bag1_name) and (bag1.name != self.bag2_name)):
			if (DEBUG):
				print("Failed mutual inclusive constraint")
				self.print_out()
			return False
		if((bag2.name == self.bag2_name) and (bag1.name != self.bag1_name)):
			if (DEBUG):
				print("Failed mutual inclusive constraint")
				self.print_out()
			return False
		return True

	def print_out(self):
		print("Mutual Inclusive Constraint: If item", self.item1_name, "is in either bag", self.bag1_name, "or bag", self.bag2_name, "then item", self.item2_name, "must be in the other bag")

"Class to represent the assignment of an item to a bag"
"item_name is the name of the item to store"
"bag_name is the name of the bag to store the item in"
"An instance of this class states that we are storing item_name in bag_name"
"If bag_name is the empty string, that means the item has yet to be assigned"
class Assignment:
	def __init__(self, item, bag):
		self.item = item
		self.bag = bag

	"Return the bag of the assignment"
	def get_bag(self):
		return self.bag

	"Return the item of the assignment"
	def get_item(self):
		return self.item

	"Set the value of the bag to the passed value, bag"
	def set_bag(self, bag):
		self.bag = bag

	def print_out(self):
		if (self.bag is None):
			print("Assignment: Item:", self.item.name, "Bag: No Bag")
		else:
			print("Assignment: Item:", self.item.name, "Bag:", self.bag.name)

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

	"Prints out all constraints"
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
		for mutual_inclusive_constraint in self.mutual_inclusive_constraints:
			mutual_inclusive_constraint.print_out()

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
		if(assignment.get_bag() == None):
			return False
	return True

"Return an unassigned variable name from the assignment list"
"assignments is the list of assignments of variables"
"returns a string"
def select_unassigned(assignments):
	for assignment in assignments:
		if(assignment.get_bag() == None):
			return assignment.item
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
def generate_domain_values(assignments, CSP):
	for item in CSP.items:
		domain = []

		for bag in CSP.bags:
			#TODO make this more intelligent, do domain specific checking
			domain.append(bag)
		item.domain = domain
	return CSP

"Order the domain values of the current variable"
"Return ordered domain"
def order_domain_values(current_variable, assignments, CSP):
	#TODO implement LCV
	for item in CSP.items:
		if (current_variable.name == item.name):	
			if (DEBUG):
				print("Ordering domain values")
			return item.domain

"Return whether or not assigning a particular variable and particular value given a particular assignment causes an inconsistency"
"Note: Some constraints may still not be satisfied, but it is important that contraints on variables (items) already assigned are satisfied"
"current_variable is the variable to be assigned (i.e. item)"
"value is the value to assign to that variable (i.e. bag)"
"assignments is the list of current item-bag assignments"
"constraints is the set of combined contraints (for the entire problem)"
"returns a boolean"
def consistent_with_constraints(current_variable, value, assignments, CSP):
	if(DEBUG):
		print("Running consistency checking")
	assigned_variables = []

	assignments = update_assignments(assignments, current_variable, value)

	if(DEBUG):
		print("--Checking consistent with constraints--")
	for assignment in assignments:
		if (assignment.bag != None):
			assigned_variables.append(assignment.item.name)

	for capacity_constraint in CSP.constraint_container.capacity_constraints:
		if (capacity_constraint.check_upper_limit(assignments, CSP.items) == False):
			assignments = update_assignments(assignments, current_variable, None)
			return False

	if(DEBUG):		
		print("Passed all capacity_constraints")
	for fit_constraint in CSP.constraint_container.fit_constraints:
		if (fit_constraint.check_upper_limit(assignments, CSP.items) == False):
			assignments = update_assignments(assignments, current_variable, None)
			return False

	if(DEBUG):		
		print("Passed all fits_constraints")
	for unary_inclusive_constraint in CSP.constraint_container.unary_inclusive_constraints:
		if (unary_inclusive_constraint.item_name in assigned_variables):	
			if (unary_inclusive_constraint.check_constraint(assignments) == False):
				assignments = update_assignments(assignments, current_variable, None)
				return False

	if(DEBUG):			
		print("Passed all unary_inclusive_constraints")
	for unary_exclusive_constraint in CSP.constraint_container.unary_exclusive_constraints:
		if (unary_exclusive_constraint.item_name in assigned_variables):
			if (unary_exclusive_constraint.check_constraint(assignments) == False):
				assignments = update_assignments(assignments, current_variable, None)
				return False

	if(DEBUG):			
		print("Passed all unary_exclusive_constraints")
	for binary_equals_constraint in CSP.constraint_container.binary_equals_constraints:
		if ((binary_equals_constraint.item1_name in assigned_variables) and (binary_equals_constraint.item2_name in assigned_variables)):
			if (binary_equals_constraint.check_constraint(assignments) == False):
				assignments = update_assignments(assignments, current_variable, None)
				return False

	if(DEBUG):			
		print("Passed all binary_equals_constraints")
	for binary_not_equals_constraint in CSP.constraint_container.binary_not_equals_constraints:
		if ((binary_not_equals_constraint.item1_name in assigned_variables) and (binary_not_equals_constraint.item2_name in assigned_variables)):
			if (binary_not_equals_constraint.check_constraint(assignments) == False):
				assignments = update_assignments(assignments, current_variable, None)
				return False

	if(DEBUG):			
		print("Passed all binary_not_equals_constraint")
	for mutual_inclusive_constraint in CSP.constraint_container.mutual_inclusive_constraints:
		if ((mutual_inclusive_constraint.item1_name in assigned_variables) and (mutual_inclusive_constraint.item2_name in assigned_variables)):
			if (mutual_inclusive_constraint.check_constraint(assignments) == False):
				assignments = update_assignments(assignments, current_variable, None)
				return False

	if(DEBUG):			
		print("Passed all mutual_inclusive_constraints")
		print("--Passed consistent with constraints--")
	return True

"Returns the passed list of assignments after updating the assignment of the passed variable"
"assignments is the current list of item-bag assignments to update"
"current_variable is the variable (item) to update"
"value is the value (bag) to assign to the variable (item)"
"returns a list of assignments"
def update_assignments(assignments, current_variable, bag):
	for assignment in assignments:
		if(assignment.item.name == current_variable.name):
			assignment.set_bag(bag)
			return assignments

"Checks if the given variable assignments satisfy all problem constraints"
"assignments is the list of item-bag assignments"
"constraints is the set of combined constraints (for the entire problem)"
"returns a boolean"
def satisfies_constraints(assignments, CSP):

	if(DEBUG):
		print("--Checking satisfies constraints--")
	for capacity_constraint in CSP.constraint_container.capacity_constraints:
		if (capacity_constraint.check_constraint(assignments, CSP.items) == False):
			return False

	if(DEBUG):		
		print("Passed all capacity_constraints")
	for fit_constraint in CSP.constraint_container.fit_constraints:
		if (fit_constraint.check_constraint(assignments, CSP.items) == False):
			return False

	if(DEBUG):		
		print("Passed all fit_constraints")
	for unary_inclusive_constraint in CSP.constraint_container.unary_inclusive_constraints:
		if (unary_inclusive_constraint.check_constraint(assignments) == False):
			return False
	if(DEBUG):
		print("Passed all unary_inclusive_constraints")
	for unary_exclusive_constraint in CSP.constraint_container.unary_exclusive_constraints:
		if (unary_exclusive_constraint.check_constraint(assignments) == False):
			return False
	if(DEBUG):
		print("Passed all unary_exclusive_constraints")
	for binary_equals_constraint in CSP.constraint_container.binary_equals_constraints:
		if (binary_equals_constraint.check_constraint(assignments) == False):
			return False
	if(DEBUG):
		print("Passed all binary_equals_constraints")
	for binary_not_equals_constraint in CSP.constraint_container.binary_not_equals_constraints:
		if (binary_not_equals_constraint.check_constraint(assignments) == False):
			return False
	if(DEBUG):
		print("Passed all binary_not_equals_constraints")
	for mutual_inclusive_constraint in CSP.constraint_container.mutual_inclusive_constraints:
		if (mutual_inclusive_constraint.check_constraint(assignments) == False):
			return False
	if(DEBUG):
		print("Passed all mutual_inclusive_constraints")
		print("--Passed satisfies constraints--")
	return True

"Run backtrack search on the passed assignment and constraints"
"assignments is the list of item-bag assignments"
"constraints is the set of combined constraints (for the entire problem)"
"returns \"failure\" if there is no possible solution with the given assignments"
"returns a list of assignments if that list satisfies all problem constraints"
def backtrack(assignments, CSP):

	if(DEBUG):
		print ("Running backtrack")

	"If every variable has been assigned, check that the assignment satisfies all constraints. If the assignment does, return it"
	if(fully_assigned(assignments)):
		if(satisfies_constraints(assignments, CSP)):
			return assignments
		else:
			return "failure"

	"Choose an unassigned variable"
	current_variable = select_unassigned(assignments)

	"Generate domain values for the chosen variable variable"
	CSP = generate_domain_values(assignments, CSP)

	"Order the domain values for the chosen variable"
	for value in order_domain_values(current_variable, assignments, CSP):
		if (DEBUG):
			print ("Testing assigning Item", current_variable.name, "to Bag", value.name)

		"Check if the value chosen is consistent with the rest of the assignments so far"
		if (consistent_with_constraints(current_variable, value, assignments, CSP)):	

			"If it is consistent, assign the variable that value to run backtrack using the new assignment"
			assignments = update_assignments(assignments, current_variable, value)
			if (DEBUG):
				print("Assigned Item", current_variable.name, "to Bag", value.name)
			result = backtrack(assignments, CSP)
			
			"If backtrack returns an assignment, we have found a solution so cascade up"
			if(result != "failure"):
				if (DEBUG):
					print("Assigned item", current_variable.name, "to bag", value.name)
				return result

			"Otherwise remove that item-bag assignment"
			assignments = update_assignments(assignments, current_variable, None)
			
		else:
			if (DEBUG):
				print("Failed to assign Item", current_variable.name, "to Bag", value.name)
	if (DEBUG):
		print("Failed with assignments")
		for assignment in assignments:
			if (assignment.bag == None):
				print ("Assignment: Item", assignment.item.name, " not in a Bag")
			else:
				print ("Assignment: Item", assignment.item.name, " in Bag", assignment.bag.name)
	"Return failure if all possible values have been checked. There is no solution for the given assignment"
	return "failure"

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
		print("Usage is py project5.py <input_file_name> [-v]")
		sys.exit()

	if(len(sys.argv) == 3):
		if(sys.argv[2] == "-v"):
			global DEBUG
			DEBUG = True

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
		temp = line.rstrip("\n").split(" ")
		items.append(Item(temp[0], temp[1]))

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
		temp = line.rstrip("\n").split(" ")
		bags.append(Bag(temp[0], temp[1]))
		
	"Update CSP"
	CSP.bags = bags
	"Reset file_content and index"
	file_content = file_content[index:]


	"Set the capacity constraints"
	for bag in bags:
		capacity_constraints.append(Capacity_Constraint(bag))

	"Update constraint_container"
	constraint_container.capacity_constraints = capacity_constraints

	"Add item fit constraints if there are any"
	if(file_content[0][0] != "#"):
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
		temp = line.rstrip("\n").split(" ")
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
		temp = line.rstrip("\n").split(" ")
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
		temp = line.rstrip("\n").split(" ")
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
		temp = line.rstrip("\n").split(" ")
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
		temp = line.rstrip("\n").split(" ")
		mutual_inclusive_constraints.append(Mutual_Inclusive_Constraint(temp[0], temp[1], temp[2], temp[3]))

	"Make sure that all constraints were parsed correctly"
	if (DEBUG):
		print("-----Printing constraints-----")
		constraint_container.print_constraints()
		print("-----Running script-----")
	"Update container"
	CSP.constraint_container = constraint_container

	"Create a list of assignments, assigning each variable to start without a bag"
	for item in items:
		new_assignment = Assignment(item, None)
		assignments.append(new_assignment)

	#TODO
	"Run backtrace using the blank assignments and the set of contraints"
	final_assignments = backtrack(assignments, CSP)

	print("-----Final Results-----")
	if (final_assignments == "failure"):
		print ("No solution found")
	else:
		for bag in bags:
			sum_items = 0
			sum_weight = 0
			string_to_output = bag.name + " "
			list_of_items = []
			for assignment in assignments:
				if(assignment.bag == bag):
					string_to_output += (assignment.item.name + " ")
					sum_items = sum_items + 1
					sum_weight = sum_weight + assignment.item.weight
			string_to_output += ("\n")
			string_to_output += ("number of items: " + str(sum_items) + "\n")
			string_to_output += ("total weight: " + str(sum_weight) + "/" + str(bag.weight) + "\n")
			string_to_output += ("wasted capacity: " + str(bag.weight - sum_weight) + "\n\n")
			print (string_to_output)


	"Handle output"

	#End TODO

if __name__ == '__main__':
	project5_main()		

