dict = {0:0,1:1}
def fib(n):
    if n  not in dict:
        val = fib(n-1)+ fib(n-2)
        print('value is-->',val)
        dict[n] = val
        print(dict[n])
    return dict[n]
n = int(input('Enter the number is ==--->>'))
print(fib(n))

