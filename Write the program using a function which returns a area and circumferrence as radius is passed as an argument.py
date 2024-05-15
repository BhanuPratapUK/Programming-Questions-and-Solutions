def caller(r):
    pi = 3.14
    return (pi*r**2,2*pi*r)
r = int(input('Enter the radius --->'))
area ,circumference= caller(r)
print('Here is the area of the circle',area)
print('The Circumference of the circle--->',circumference)