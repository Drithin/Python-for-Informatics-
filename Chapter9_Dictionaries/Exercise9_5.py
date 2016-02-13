fh = open('mbox-shortS.txt')

countDict = dict()

for line in fh:
	line = line.rstrip()
	if line.find('From ') == -1:
		continue
	a = line.find('@')
	b = line[a+1, line.endswith(' ')]
	c = b.strip()

	for i in c:
		if i not in countDict:
			countDict[i] = 1
		else:
			countDict[i] += 1
print countDict