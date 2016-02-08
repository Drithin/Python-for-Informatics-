S = str(raw_input('Enter the String :'))
A = str(raw_input('Enter the letter :'))

def counting(S, A):
	count = 0

	for letter in S:
		if letter == A:
			count += 1
	print count

counting(S,A)