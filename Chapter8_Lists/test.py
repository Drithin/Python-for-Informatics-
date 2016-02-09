def listNumber():
	b = 0

	empList = []

	while True:
		a = raw_input('Enter the number : ')

		if a == 'done':
			print empList
			print 'Maximum : ', max(empList), "Minimum : ", min(empList)
			break
		else:
			try:
				#b += float(a)
				empList.append(a)
			except:
				print('Invalid Input')

listNumber()