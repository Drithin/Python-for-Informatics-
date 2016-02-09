fileName = raw_input('Enter the file name: ')

try:
	f = open(fileName, "r")
except:
	print "File Doesnt exist"

count = 0
sumTotal = 0

for line in f:
	line = line.rstrip()
	if line.find("X-DSPAM-CONFIDENCE:") == -1:
		continue
	a = line.find(':')
	b = line[a+1:len(line)-1]
	c = b.strip()
	d = float(c)

	sumTotal += d
	count = count + 1

print 'Average Spam Confidence: ', (sumTotal/count)




	
		
		

