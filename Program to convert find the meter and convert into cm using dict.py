cm={x:x*100 for x in range(1,6)}
z= cm.values()
m= {y/100 for y in z}
print('Here the list of Centimeter -->',cm)
print('Here the list of Meter -->',m)