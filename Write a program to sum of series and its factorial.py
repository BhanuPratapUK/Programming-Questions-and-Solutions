def check(num):
    fact=1
    if num==1:
        return 1
    else:
        for i in range(1,num+1):
            fact=fact*i
        return fact
A=0
n=int(input('The Number is=--->'))
for i in range(n+1):
        A+=i**i//check(i)
print(A)


