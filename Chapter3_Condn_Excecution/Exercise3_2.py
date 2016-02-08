try:
    hours = float(raw_input('Enter Hours: '))
    rate = float(raw_input('Enter Rate: '))
    Overtime_rate = 1.5

    def payableAmount(hours, rate):
	overtime_pay = 0

	if hours > 40:
		extra_hours = hours - 40
		overtime_pay = extra_hours * rate * Overtime_rate
		final_pay = ((hours - extra_hours) * rate) + overtime_pay
	else :
		final_pay = (hours*rate)
		
	return "Pay:" + str(final_pay)

    print payableAmount(hours, rate)

except:
	print('Please enter an integer')
 
	



