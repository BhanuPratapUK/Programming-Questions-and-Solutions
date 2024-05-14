import random
list1 = []
for i in range(10):
    x = random.randint(1,100)
    list1.append(x)
print(list1)
even=[]
odd =[]
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print('Her is the list of random EVEN numbers->',even)
print('Her is the list of random ODD numbers->',odd)
'''Everytime you run it gonna bring the new 10 random number from 1 -100'''
    