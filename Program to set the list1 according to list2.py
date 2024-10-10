x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [0,   1,   1,    0,   1,   2,   2,   0,   1]
a = list(set(y))
a.sort()
new= []
for i in a:
    for j in range(0,len(y)):
        if y[j]==i:
            new.append(x[j])
print('Here is the New list according to Second one ---->',new)
