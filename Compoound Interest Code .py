p=int(input('The Principal is-->'))
r=int(input('The interest rate is -->'))
time=int(input('The Period for the investment will be-->'))
amount=p
for i in range(1,time+1):
    amount*=(1+r/100)
    print(i,'year the interest+ principal is -->',amount)

