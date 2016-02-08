def readNumber2():
	num = []
	fullCount = 0
	while True:
		numbr = raw_input("Enter a number : ")
		if numbr == 'done':
			print min(num), max(num)
			break
		else:
			try:
				num.append(float(numbr))
			except:
				print "Invalid Input"
				continue
readNumber2()
