"arkessler & irshusdock"
"Alexi Kessler & Ian Shusdock"

import sys

"Main script for the program"
def project5_main():
	
	f = open(sys.argv[1])
	file_content = f.readlines()
	f.close()
	
	count = 0
	for line in file_content:
		if(line[0] == "#"):
			count = count + 1
		
	
	