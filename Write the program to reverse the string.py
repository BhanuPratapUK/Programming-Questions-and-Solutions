def string(Text):
    New_string =""
    i = len(Text)-1
    while i>=0:
        New_string +=Text[i]
        i-=1
    return New_string
Text = input('PLease write down the message you wanna reverse ---->')
print('See the Result--->',string(Text))