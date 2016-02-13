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
print countings

#fhand = open('mbox-shortS.txt')

#counts = dict()
#for line in fhand:
	#line = line.rstrip()
	#if not line.startswith('From'): continue
	#wrds = line.split()
	#for wrd in wrds:
		#if wrd not in counts:
			#counts[wrd] = 1
		#else:
			#counts[wrd] += 1

#print counts6