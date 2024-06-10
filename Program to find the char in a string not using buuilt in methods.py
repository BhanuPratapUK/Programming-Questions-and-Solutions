def find_chr(s,c):
    count=0
    for i in range(len(s)):
        if s[i]==c:
            return i
        else:
            pass
s= 'god is great'
c='r'
print('The index of a character we are looking for is present at -->',find_chr(s,c))