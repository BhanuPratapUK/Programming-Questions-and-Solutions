dict1 = {'bhanu':[55,55],'akash':[55,66]}
total = {}
tot = 0
for key ,val in dict1.items():
    tot = sum(val)
    total[key] = tot
print(total)
max = 0
for key , val in total.items():
    if val > max:
        max = val
        topper = key
print(topper,'is standing overhere',max)