''' 
Suppose we get a object in float and we want the value upto 2 or 3 decimal so we can use 
"format"  method there is another method known as round method.
format(value, format specifier)
round(format(value, format specifier))
'''
x = 10/3
print('Here is the answer without using any method-->',x)
y = format(x,'.2f')
print('Here is the answer using any method--->',y)