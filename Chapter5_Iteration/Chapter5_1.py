def readNumber():
	totalCount = 0
	totalSum = 0

	while True:
		num = raw_input("Enter a number :")

		if num == 'done':
			print totalSum, totalCount, (totalSum/totalCount)
			break
		else:
			try:
				totalSum += float(num)
			except:
				print('Invalid Input')
				continue
		totalCount += 1

readNumber()
