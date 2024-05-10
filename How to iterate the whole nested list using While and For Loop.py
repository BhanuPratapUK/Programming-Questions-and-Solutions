List1= [1,2,3,4,5]#here is the list
List1[3]= ['Hi','Bhanu','How','are','you',10,20]#New list
'''Here Using FOR Loop '''
for x in List1:
    print(x)# whole list will be iterated including nested also
'''Here next one using WHILE loop'''
i = 0
while i<(len(List1)):
    print('On',i,'The element is present is=>',List1[i])
    i+=1
'''Here we Gonna Iterate the nested list using FOR loop '''
for x in List1[3]:
    print(x)
'''Here we Gonna Iterate the nested list using WHILE loop '''
i = 0
while i<(len(List1[3])):
    print('On',i,'The element is present is nested list=>',List1[3][i])
    i+=1


