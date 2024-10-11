text = [1,2,(),3,4,6,(),56,23,1,0,False,2,3,[],4]
x = filter(None,text)
print('Remove the empty tuples',list(x))
