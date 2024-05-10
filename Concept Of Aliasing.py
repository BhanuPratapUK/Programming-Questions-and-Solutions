List1= [5,6,1,2,10,11,13,3,3,6,8]
List2=List1
print(List1)
print(List2)
print('After Updation')
List2[3]= 'LEMON'
print(List1)
print(List2)

print(id(List1))
print(id(List2))
print(List1==List2)

#Theory--
'''As you can see the i just made a New object named as a List2 and put an equal to a list1. From this point 
we can have scenerio that list2 = list1 but list1 not get copied in list2.So what happened here
there is two object list1 and list2 refering the same object --->[5, 6, 1, 2, 10, 11, 13, 3, 3, 6, 8]
list1--------
              [5, 6, 1, 2, 10, 11, 13, 3, 3, 6, 8]
list2--------
there are just refering the same object and how can we get to know by  using ID function 
on both list1 and list2 '''

