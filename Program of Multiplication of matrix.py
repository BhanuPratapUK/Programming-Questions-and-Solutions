x= [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

z=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(3):
    for j in range(3):
        z[i][j]= x[i][0] * y[0][j]+ x[i][1] * y[1][j]+x[i][2] * y[2][j]
print('The Result is --->',z)