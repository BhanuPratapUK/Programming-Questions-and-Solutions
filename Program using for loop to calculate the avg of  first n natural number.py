num = int(input('Enter the numbers-->'))
avg = 0
sum = 0
for i in range(1,num+1):
    sum+=i
    avg = sum/num
print('The sum of N Numbers',sum)
print('The Average of the number s are -->',avg)