#Week 3 21092019

# x = int(input("Please enter an integer: "))

# if x < 0:
# 	x = 0
# 	print("Negative changed to zero")
# elif x == 0:
# 	print("Zero")
# elif x == 1:
# 	print("Single")
# else:
# 	print("More...")


# x = int(input("Please Enter your age: "))

# if x < 40 and x > 10:
# 	print('Go to the beach...')
# elif x > 40 and x < 75:
# 	print('Go to the bagan...')
# elif x > 3 and x < 10:
# 	print('Go to the Happy World..')
# else:
# 	print('Unlisted...')

m = int(input('Examination Result: '))

if m == 100:
	print('Scholar')
elif m >= 70:
	print('Distnction')
elif m < 70 and m >= 50:
	print('Excellent')
elif m < 50 and m >= 40:
	print('Pass!')
elif m < 39 and m >= 35:
	print('Mod!')
elif m < 35 and m >= 10:
	print('Fail!')
elif m <= 10:
	print('Warning!')
else:
	print('Wrong input..')

