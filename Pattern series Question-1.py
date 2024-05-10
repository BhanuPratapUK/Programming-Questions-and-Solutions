#Pattern Questions Number---1

for i in range(1,7):
    Text= 'A'
    print()
    for j in range(i):
        print(Text,end='')
        Text= chr(ord(Text)+1)

'''     
Here is  the pattern we have to make and you will get this
I have used ord and chr method and updating the Text everytime

A
AB
ABC
ABCD
ABCDE
ABCDEF
'''
