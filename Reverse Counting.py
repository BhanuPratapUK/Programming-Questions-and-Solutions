def reverse_number(num):
    while num>0:#  case-1=10>0 True and so on...
        print(num,end=' ')#10,.....etc till 1 because num should be greater than 0 
        # we used end='' beacuse I want to print the all numbers horizontally as you can see 
        num-=1#num= 10-1 num=9 we are updating num here nad so on.... 
num = int(input('Here Enter the digit upto What you want Reverse Counting=>'))
reverse_number(num)
# if you enter num= 10 
# The output will be as like this => 10 9 8 7 6 5 4 3 2 1
# Thank you

