def number(n):
    count = 0#count method to count how many times it got divided during iteration 
    for i in range(2,n+1):# 1 is not a prime number  so we should started with 2 and divisible by upto itself 
        if n%i==0:
            count+=1
    return count
num= int(input('Enter the Number =>>'))
result = number(num)
if (result ==1):
    print('The number you inserted is PRIME')
else:
    print('The number you inserted is NOT Prime and  it is Compostie number ')