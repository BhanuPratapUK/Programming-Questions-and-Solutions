def  fibonacci(x):
    a = 0
    b=1
    list1 = [0,1]
    for i in range(2,x+1):
        s= a+b
        a=b
        b=s
        list1.append(b)
    print(list1)
fibonacci(5)