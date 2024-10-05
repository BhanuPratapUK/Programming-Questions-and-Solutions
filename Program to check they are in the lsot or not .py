def check(x,list1):
    for i in list1:
        if x == i:
            return True 
    return False
x=  int(input('Enter the Number you Are looking for -->'))
list1= [1,2,3,4,5,6,7,7,9,0,12,14]
print('SO Here it is -->',check(x,list1))