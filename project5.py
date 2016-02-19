"arkessler & irshusdock"
"Alexi Kessler & Ian Shusdock"

import sys


class Variable:
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight

"Main script for the program"
def project5_main():
	
	f = open(sys.argv[1])
	file_content = f.readlines()
	f.close()
	
	file_content = file_content[1:]

	variables = []
	index = 0

	for line in file_content:
		if(line[0] == "#"):
			break
		variables.append(Variable(line[0], line[2]))






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