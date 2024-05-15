tup = (1,2,3,4,5)
del tup[3]
print(tup)

''' It will show this type of error---> REASON is tuple is a IMMUTABLE it cannot be update or delete any  element from it
but we can delete the entire  list of tuple by using del method  you wil
del tup [3]
        ~~~~^^^
TypeError: 'tuple' object doesn't support item deletion'''
tup = (1,2,3,4,5)
del tup
print(tup)
'''
but we can delete the entire  list of tuple by using del method  you will get this output
 print(tup)
          ^^^
NameError: name 'tup' is not defined
'''