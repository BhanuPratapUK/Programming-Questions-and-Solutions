List= [2,5,8,10,15]
print('Here the length of the list  I gonna use to calculate the Average -> ',len(List))
Sum = 0
Mean= 0
for i in List:
    Sum+=i
    Mean=Sum//len(List)
print('The Sum of the  list-->',Sum)
print('The Average the List is -->>',Mean) 
