file1 = raw_input('Enter the file name: ')

def fileName(file1):
	fh = open(file1, "r")

	el = []

	for line in fh:
		f = line.split()
		el.extend(f)
		el.sort()
	print el

fileName(file1)
