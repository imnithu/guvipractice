a=int(input("Enter the first hour"))
b=int(input("Enter the first minute"))
c=int(input("Enter the second hour"))
d=int(input("Enter the second minute"))
e=a*60+b
f=c*60+d
g=e-f
print(g//60 'hr',g%60'min')
