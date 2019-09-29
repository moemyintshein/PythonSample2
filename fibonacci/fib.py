from __future__ import print_function 

def fibo(n):
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a + b
	print()




					
# result		a		b (a+b)
# 0			0		1
# 1			1		1
# 1			1		2
# 2			2		3


def fib2(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result