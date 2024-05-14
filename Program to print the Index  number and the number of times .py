list1 = [10,11,12,13,14,10,18,14]
num = int(input('Find the numbeer is=>>'))
count=0
for i in range(len(list1)):
    if list1[i] == num:
        count+=1
        print(num,'it is present at this  index=>>',i)
print(num,'total number of times came in a list =>>',count)
