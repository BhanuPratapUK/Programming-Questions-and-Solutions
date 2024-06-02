a = int(input('Enter thr number is--->'))
b = int(input('Enter thr number is--->'))
c = int(input('Enter thr number is--->'))
d = int(input('Enter thr number is--->'))
big = 0
if a > b:
    big = a
    if a > c:
        big = a
        if a > d:
            big = a
            print('A is big than -<>',big)
        else:
            big = d
            print('D is BIG THAN ',big)
else:
    if b > c:
        big = b
        if b > d:
            big = b
            print('B is big than--',big)
        else:
            big = d
            print('D is big than ',big)
    else:
        if c >d:
            big = c
            print('C id big thasn ',big)
        else:
            big = d
            print('D is big than ',big)


