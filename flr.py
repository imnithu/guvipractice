import math
p=int(input("Enter Principal Amount P"))
t=int(input("Enter Time T"))
r=int(input("Enter Rate R"))
a=p*t*r/100
print('Floor value=',math.floor(a))
