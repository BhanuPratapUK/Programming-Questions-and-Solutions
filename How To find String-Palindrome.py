def str_palin(msg):
    if (msg==msg[::-1]):
        return 1

msg = input('Enter the String You wanna find it is palindrome or not=>>')
result = str_palin(msg)
if result ==1:
    print('The String is Palindrome')
else:
    print('The string is not Plaindrome')
