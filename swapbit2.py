a=int(input("Enter a number"))
b=int(input("Enter another number"))
print(a,b)
a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)
