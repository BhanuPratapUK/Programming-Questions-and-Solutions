a =[[1,2,3],
    [4,5,6],
    [7,8,9]
]
b = [
    [11,12,13],
    [14,15,16],
    [17,18,19]
]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        result[i][j]= a[i][j]+ b[i][j]
        print(result)
for x in result:
    print(x)