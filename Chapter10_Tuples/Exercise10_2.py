fha = open('mbox-shortS.txt')

countings = dict()

for li in fha:
	li = li.rstrip()
	if not li.startswith('From '):continue
	wrds = li.split()
	reqwords = wrds[5]

	hour, minute, year = reqwords.split(':')

	for i in hour:
		if i not in countings:
			countings[i] = 1
		else:
			countings[i] += 1

l = list()

for key,val in countings.items():
	l.append((key,val))

l.sort()

print l
