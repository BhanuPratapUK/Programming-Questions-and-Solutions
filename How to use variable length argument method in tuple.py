def func(*val):
    print(val)
val=(1,2,3,4)
func(val)
''' * is called  Gather  and its opposte is scatter  aas you can see  in next program '''
var= (100,3)
quo,rem = divmod(*var) 
print(quo)
print(rem)