a = int(input('Enter thr number is--->'))
b = int(input('Enter thr number is--->'))
c = int(input('Enter thr number is--->'))
d = b*b - 4*a*c
x = 2*a
if d>0:
    R1= (-b+d**0.5)/x
    R2= (-b-d**0.5)/x
    print('root1->',R1,'and','root2 is->',R2)
elif d==0:
    root1 = -b/x
    print('root1 and root2 is -->',root1)
else:
    print('Here it is a IMAGINARY LINES')

