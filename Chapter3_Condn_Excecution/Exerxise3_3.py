try:
    score = float(raw_input('Enter your score: '))

    while  score != "":
	    score = float(raw_input('Enter your score: '))

    if score >= 0.9:
	    print ('A')
    elif score >= 0.8 and score < 0.9:
	    print ('B')
    elif score >= 0.7 and score < 0.8:
	    print ('C')
    elif score >= 0.6 and score < 0.7:
	    print('D')
    elif score < 0.6:
	    print('F')

except:
	print ('Please enter a float numbered score')
