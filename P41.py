a=int(input('ENTER N'))
h=int(input('ENTER K'))
b=a*h
i=0
f=[]
while b>0:
    n=i*i
    f.append(n)
    i=i+h
    b=b-1
if a in f:
    print("YES")
else:
    print("NO")
