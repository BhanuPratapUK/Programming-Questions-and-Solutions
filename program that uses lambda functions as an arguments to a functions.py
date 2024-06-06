def func(a,b):
    print('Answer is ---->',a(b))
twice= lambda x : x**3
thrice = lambda y : y**3
func(twice,4)
func(thrice,5)