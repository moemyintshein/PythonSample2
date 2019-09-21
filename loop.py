>>> words = ['cat', 'wondow', 'defenestrate', 'world']
>>> for w in words:
...     print(w, len(w))
... 
cat 3
wondow 6
defenestrate 12
world 5

>>> words = ['cat', 'wondow', 'defenestrate', 'world']
>>> for w in words:
...     print(w)
... 
cat
wondow
defenestrate
world


>>> words = ['cat', 'wondow', 'defenestrate', 'world']
>>> for w in words[:]:
...     if len(w) > 6:
...             words.append(w)
... 
>>> words
['cat', 'wondow', 'defenestrate', 'world', 'defenestrate']
>>> words = ['cat', 'wondow', 'defenestrate', 'world']
>>> for w in words[:]:
...     if len(w) > 4:
...             words.insert(0, w)
... 
>>> words
['world', 'defenestrate', 'wondow', 'cat', 'wondow', 'defenestrate', 'world']
>>>