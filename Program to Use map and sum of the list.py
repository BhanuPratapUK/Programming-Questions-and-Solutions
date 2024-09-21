def squares(x):
    return (x**2)
list1 = list(map(squares,range(1,10)))
print(list1)
sum=0
for i in list1:
    sum+=i
print('The list1 after using map function and sum of the squares-->',sum)