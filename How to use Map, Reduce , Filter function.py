def operate(x):
    if x%2==0 :
        return 1
result = list(filter(operate,range(1,10)))# Filter function basically give the boolean values
print(result)

print('**************************************')

def modifying(y):
        return y+3
result1 = list(map(modifying,range(2,12))) # Map function  just modify the values
print(result1)

print('**************************************')
import functools
def modifying(z,a):## Reduce totally based on two digit  and we have to use the functools on this
     return z+a## it return the single digit 
result3 = functools.reduce(modifying,range(1,19))
print(result3)

