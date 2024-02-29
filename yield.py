def myfunc():
    print('Before first yield.')
    yield 'First yield.'
    print('After first, before second yield.')
    yield 'Second yield.'
    print('After second yield.')
    
"""
g = myfunc()
next(g)
Before first yield.
'First yield.'
next(g)
After first, before second yield.
'Second yield.'
next(g)
After second yield.
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
builtins.StopIteration:
for s in myfunc():
   print('dostal jsem te, s')

Before first yield.
dostal jsem te, s
After first, before second yield.
dostal jsem te, s
After second yield.
for s in myfunc():
   print('dostal jsem te', s)

Before first yield.
dostal jsem te First yield.
After first, before second yield.
dostal jsem te Second yield.
After second yield.

g = myfunc()
list(g)
Before first yield.
After first, before second yield.
After second yield.
['First yield.', 'Second yield.']
"""