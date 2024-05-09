Text = input('Write Down the Text to remove the vowels from it=>')
for x in Text:
    if x not in 'AEIOUaeiou':
        print(x,end=' ')