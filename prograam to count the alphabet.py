string  ="ALPHABET"
list1 = []
count = 0
for i in string:
    if i in "AEIOUaeiou":
        list1.append(i)
        count+=1
print('The vowels in alphabet-->>',count)
print('The vowels arre present in a string-->',list1)
