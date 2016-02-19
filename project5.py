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
	
	