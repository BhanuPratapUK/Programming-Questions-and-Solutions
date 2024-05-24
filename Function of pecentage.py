def percen(phy,chem,bio):
    total = (phy+chem+ bio)*100/300
    return total
phy = int(input("Enter the Physics number -->"))
chem= int(input("Enter the chemistry number -->"))
bio = int(input("Enter the biology number -->"))
print("The percentage is -->>",percen(phy,chem,bio),'%')
