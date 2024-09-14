def function(x,c,beg=0):
    count=0
    for i in range(beg,len(x)):
        if x[i]==c:
            count+=1
        else:
            pass
    return count
x=input('The string is -->')
c= input('The Character is -->')
print('The ',c,'comes in the stirng is -->',function(x,c))
loc= int(input('start the string form here'))
print('The begining of the word is start form->',loc,'and',c,'striing will be in this string-->',x,'--->',function(x,c,loc))
