dict1= {0:0,1:1}
def fibnacci(n):
    if n not in dict1:
        value = fibnacci(n-1) + fibnacci(n-2)
        dict1[n]= value
    return dict1[n]
n = int(input('Enter the value ->'))
print('Here is the answer-->',fibnacci(n))