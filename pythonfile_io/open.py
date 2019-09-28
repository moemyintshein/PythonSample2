#Week 4B 28092019

# f = open('test.txt', 'r')

# print(f.name)

# f.close()
from __future__ import print_function   #for end function working


# with open('test.txt', 'a+') as f:
	# f_text = f.readline()
	# print(f_text, end='')

	# f_text = f.readline()
	# print(f_text, end='')
# 	f.write('6.This is line number 6.'+"\n")
	

# with open('test.txt', 'r') as f:
# 	for line in f:
# 		print(line, end='')


	# f_text = f.read(500)
	# print(f_text, end='')

# with open('test.txt', 'a') as g:
	
# 	print(i, end='')

with open('test.txt', 'r') as f:
	size_to_read = 500
	f_text = f.read(size_to_read)

	while len(f_text) > 0:
		print(f_text, end='')
	

