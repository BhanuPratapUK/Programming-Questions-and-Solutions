msg = 'hey bhnau how are you'
msg = msg.lower()
dict1 = {}
for i in msg:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] = dict1[i]+1
print(dict1)
for key, value in dict1.items():
    print(key,'multiply','1'   * value)