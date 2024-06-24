list1 = ['Boy','hat','apple','nail','umbrella']
New_list  =[]
for i in list1:
    New_list.append(i[0])
print('The fist charcter of the list1-->>',New_list)


print('**************************************************')
# we can do by iterate also 
list1 = ['Boy','htot','apple','nail','umbrella']
New_list  =[]
for i in range(len(list1)):
    New_list.append(list1[i][0])
print('Here the  new list by iterating the list->>',New_list)