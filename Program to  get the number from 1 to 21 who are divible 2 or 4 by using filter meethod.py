def func(x):
    if x%2==0 or x%4==0:
        return True
my_list= list(filter(func,range(1,21)))
print('Here the list who are divisible by 2 or 4 -->',my_list)