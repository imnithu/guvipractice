def gcd(x, y):
    if x > y:
        a = y
    else:
        a = x
    for i in range(1, a+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    return hcf
b =int(input("Enter a number")) 
c= int(input("Enter a number")) 
print(gcd(b,c))
