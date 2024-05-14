list1 = []
start = int(input('Start from =>>'))
stop = int(input('Stop at =>>'))
step = int(input('gap should be=>>'))
for i in range(start,stop,step):
    list1.append(i)
print(list1)
i= len(list1)-1
while i>=0:
    print(list1[i],end=' ')
    i-=1
#In the end i just reverse it 
