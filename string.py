#Week 2A 14.09.2019

print('"I can do everything Nothing Impossible"')
print("'I can do everything Nothing Impossible'")

x = "hello world"
print(x)

>>> x = 'Hello' + ' ' + 'World'
>>> x
'Hello World'
>>> 5 * 'Hello' + 'World'
'HelloHelloHelloHelloHelloWorld'
>>> 'Hello' + str(1)
'Hello1'
>>> 'Hello' * 3
'HelloHelloHello'
>>> int("3") + 3
6


P r o g r a m m i n g
0 1 2 3 4 5 6 7 8 9 10

>>> x = 'Programming'  #string
>>> x[6]
'm'
>>> x[0]
'P'
>>> x [0:6]
'Progra'
>>> x [1:5]
'rogr'
>>> x [:7]
'Program'
>>> x [8:]
'ing'
>>> x [:]
'Programming'
>>> x [-4]
'm'
>>> x [5:-4]
'am'
>>> x[:3] + x[4:]
'Proramming'
>>> x[:3] * 5
'ProProProProPro'
>>> x[:3] + ' ' * 5
'Pro     '
>>> (x[:3] + ' ') * 5
'Pro Pro Pro Pro Pro '
>>> x[0] = 'Q'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> x[0:4] + 'ram'
'Program'
>>> x[0:5] + 'Python'
'ProgrPython'
>>> len(x)
11
>>> len(x) + 4
15
>>> len(x[5]) + 4
5
>>> len(x[5])
1
>>> len(x[5:9]) + 4
8

>>> x = 'Programming'  #string
>>> word = [1, 3, 5, 7, 9, 11, 13, 15]  #list
>>> word
[1, 3, 5, 7, 9, 11, 13, 15]
>>> word[5]
11
>>> word[5:7]
[11, 13]
>>> word = ['P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
>>> word[0] = 'Q'
>>> word
['Q', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
>>> word[:] = 'Good'
>>> word
['G', 'o', 'o', 'd']
>>> word[2]
'o'

>>> word = [1, 3, 5, 7, 9, 11, 13, 15]
>>> word + word
[1, 3, 5, 7, 9, 11, 13, 15, 1, 3, 5, 7, 9, 11, 13, 15]
>>> word[:] + [2, 4, 6, 8, 10]
[1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10]


>>> a = [1, 3, 5, 7, 9]
>>> b = [2, 4, 6, 8, 10]
>>> c = ["A", "B", "C", "D", "E"]
>>> x = a + b + c
>>> x
[1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 'A', 'B', 'C', 'D', 'E']
>>> x = [a, b, c]
>>> x
[[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], ['A', 'B', 'C', 'D', 'E']]
>>> x[1:3]
[[2, 4, 6, 8, 10], ['A', 'B', 'C', 'D', 'E']]
