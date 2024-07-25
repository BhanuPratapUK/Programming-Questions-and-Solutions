num  = int(input('Enter the number-->'))
composite = 0
for i in range(1,num):
    if num%i==0:
        composite=1
        break
if composite==1:
    print('This is number is not a PRIME number')
else:
    print('This is a a Prime Number')