hours = float(raw_input('Enter hours: '))
rate = float(raw_input('Enter rate: '))

def computepay(hours, rate):
	otPay = 0

	if hours > 40:
		othours = hours - 40
		otPay = othours * rate * 1.5
		pay = hours * rate
		fullPay = ((hours - othours) * rate)+ otPay
		

	else:
		fullPay = hours * rate
	
	return "Pay:", str(fullPay)

print computepay(hours, rate)

