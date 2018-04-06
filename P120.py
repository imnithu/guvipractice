n=int(input("Enter any number"))
b=0
while(n>0):
    a=n%10
    b=b+a**2
    n=n//10
print("The total sum of squares of digits is:",b)
