def squares(x):
    return (x**2)

list1 = list(map(squares,range(1,11)))
print('List of squares form 1- 10->',list1)
add =0
for i in list1:
    add+= i
print('The total summ of alll the numbers is  -->',add)


