print("________Enter the -1 'Exit'to go out of it____________")
circumference = {}
while True:
    radius = int(input('Enter the  number is  --->>'))
    if radius == -1:
        break
    else:
        list1 = {radius : 2*3.14*radius}
        circumference.update(list1)
print(circumference)