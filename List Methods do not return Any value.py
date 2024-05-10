#REMOVE Method
List1 =[11,12,13,14,15,16,17,18]
print(List1.remove(16))## will return NONE but it will remove it the object 
#Correct way to Implement thre 'REMOVE' method
List1.remove(15)#we have taken another object because 16 is already  removed if we remove againg there will error ike The element not in a list 
print(List1)##Try both methods you will see the difference
###################################################################
##SORT Method
List2 =[100,2,36,7,23,33,45,56,67]
print(List1.sort())## will return NONE
#Correct way to Implement thre 'SORT' method
List2.sort()
print(List2)##Try both methods you will see the difference
###################################################################
##INSERT Method
List2 =[100,2,36,7,23,33,45,56,67]
print(List1.insert(0,100000))## will return NONE
#Correct way to Implement thre 'INSERT' method
List2.insert(2,100000)
print(List2)##Try both methods you will see the difference




