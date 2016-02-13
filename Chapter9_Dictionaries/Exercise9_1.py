f = raw_input('Enter file name :')

fhand = open(f, "r")

text = fhand.read()

words = text.split()

newDict = dict()

for word in words:
	newDict[word] = None

print newDict

g = raw_input('Enter Key value :')

print g in newDict

