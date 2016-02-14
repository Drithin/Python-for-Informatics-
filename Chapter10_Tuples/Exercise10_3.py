import string

fhand = open('words.txt') 

counts = dict()

for line in fhand:
	line = line.lower()
	l = tuple(line)

	for w in l:
		if w not in counts:
			counts[w] = 1
		else:
			counts[w] += 1
l = list()

for key,val in counts.items():
	l.append((val, key))

l.sort(reverse=True)

for key, val in l:
	print key, val