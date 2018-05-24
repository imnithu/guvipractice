a=list(input("Enter any list of numbers"))
b=a[:len(a)//2]
c=a[len(a)//2:]
b.sort()
d=sorted(c,reverse=True)
e=b+d
print("".join(e))
