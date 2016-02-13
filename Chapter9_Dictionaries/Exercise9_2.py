fha = open('mbox-shortS.txt')

countings = dict()

for li in fha:
	li = li.rstrip()
	if not li.startswith('From '):continue
	wrds = li.split()
	reqwords = wrds[2]

	for wrd in reqwords:
		if wrd not in countings:
			countings[wrd] = 1
		else:
			countings[wrd] += 1
print countings
	#wrds = li.split()
	#print wrds[2]
	#for wrd in wrds:
		#if wrd not in counts:
			#counts[wrd] = 1
		#else:
			#counts[wrd] += 1
