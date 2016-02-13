fha = open('mbox-shortS.txt', 'r')


for li in fha:
	li = li.rstrip()
	if li.startswith('From '):
		print line