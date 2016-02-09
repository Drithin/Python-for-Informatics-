fileName = raw_input('Enter the file name: ')

try:
	f = open(fileName, "r")
except:
	print "File Doesnt exist"

for line in f:
	line = line.rstrip()
	print line

