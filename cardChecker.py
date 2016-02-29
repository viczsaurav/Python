# Basically, the algorithm takes each digit, from right to left and muliplies each second
# digit by two. If the multiple is two-digits long (i.e.: 6 * 2 = 12) the two digits of
# the multiple are then added together for a new number (1 + 2 = 3). You then add up the
# string of numbers, both unaltered and new values and get a total sum. This sum is then
# divided by 10 and the remainder should be zero if it is a valid credit card. Hense the
# name Mod 10 or Modulus 10. */

def checkValidCardNumber(ccNumb):
	valid = "0123456789"  		# Valid digits in a credit card number
	cardLen = len(ccNumb) 		# The length of the submitted cc number
	iCCN = int(ccNumb) 			# integer of ccNumb
	sCCN = str(ccNumb)			# string of ccNumb
	sCCN = sCCN.strip() 		# strip spaces
	iTotal = 0 					# integer total set at zero
	bNum = True 				# by default assume it is a number
	bResult = False 			# by default assume it is NOT a valid cc

# Determine if the ccNumb is in fact all numbers
	if not str.isnumeric(ccNumb):
		bNum = False

	# Determine if it is the proper length
	if((cardLen == 0) and (bResult)):				 			# nothing, field is blank AND passed above # check
		bResult = false;
	else:
		if(cardLen >= 15):										# 15 or 16 for Amex or V/MC
			for _ in range(cardLen):							# LOOP throught the digits of the card
				calc = int(iCCN % 10)							# right most digit
				iTotal += calc; 								# running total of the card number as we loop - Do Nothing to first digit
				#i = i-1
				iCCN = iCCN / 10; 								# subtracts right most digit from ccNumb
				calc = int(iCCN) % 10 ; # NEXT right most digit
				calc = calc *2; # multiply the digit by two
				#Instead of some screwy method of converting 16 to a string and then parsing 1 and 6 and then adding them to make 7,
				# I use a simple if-elif statement to change the value of calc2 to 7 if 16 is the multiple.
				if calc==10:
					calc=1			#5*2=10 & 1+0 = 1
				elif calc==12:
					calc=3			#6*2=12 & 1+2 = 3
				elif calc==14:
					calc=5			#7*2=14 & 1+4 = 5
				elif calc==16:
					calc=7			#8*2=16 & 1+6 = 7
				elif calc==18:
					calc=9			#9*2=18 & 1+8 = 9
				else:
					calc=calc		#4*2= 8 & 8 = 8 -same for all lower numbers
				iCCN = iCCN / 10 	# subtracts right most digit from ccNum
				iTotal += calc  	# running total of the card number as we loop
			# End Of Loop
			if ((iTotal%10)==0): 	# check to see if the sum Mod 10 is zero
				bResult = True 		# This IS (or could be) a valid credit card number.
			else:
				bResult =False   	# This could NOT be a valid credit card number
	if bResult:
		print('{0}'.format(ccNumb)) # Only print Valid Card Numbers

if __name__ == '__main__':
	with open('cardNumber.in') as f:
		cardList = f.readlines()
	for card in cardList:
		#print(card.split( )[1])
		checkValidCardNumber(str.strip(card.split( )[1]))