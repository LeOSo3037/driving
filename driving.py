country = input('Please enter your country')
age = input('How old are you?')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You can drive ~~~~~' )
	else:
		print('You can not QQ')
elif country == 'USA':	
	if age >= 16:
		print('You can drive ~~~~~' )
	else:
		print('You can not QQ')
else:
	print('You can only search for Taiwan or USA')
