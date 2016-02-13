fha = open('mbox-shortS.txt')

countings = dict()

for li in fha:
	li = li.rstrip()
	if not li.startswith('From '):continue
	wrds = li.split()
	reqwords = wrds[1]

	for wrd in reqwords:
		if wrd not in countings:
			countings[wrd] = 1
		else:
			countings[wrd] += 1

maxKey = max(countings, key=countings.get)

print(maxKey, countings[maxKey])
