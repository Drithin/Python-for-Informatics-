def listNumber():
	b = 0

	empList = []

	while True:
		a = raw_input('Enter the number : ')

		if a == 'done':
			floatList = map(float, empList)
			print 'Maximum : ', max(floatList), "Minimum : ", min(floatList)
			break
		else:
			try:
				#b += float(a)
				empList.append(a)
			except:
				print('Invalid Input')

listNumber()