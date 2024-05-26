dict1= {'class':12,'name': 'Bhanu','roll_no':233}
inverted = {}
for key ,value in dict1.items():
    inverted[value] = key
print(dict1)
print(inverted)