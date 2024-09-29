def function(x,y):
    new = []
    for i in range(x,y+1):
        if (i==0) or (i ==1):
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i%j==0:#11
                    break
            else:
                new.append(i)
    return new

x = int(input('Enter the starting digit-->'))
y = int(input('Enter the ending digit-->'))
list1 = function(x,y)
if len(list1)==0:
    print('This is no Prime Numbers')
else:
    print('Here is thee list og prime numbers-->',list1)

            

