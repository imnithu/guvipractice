n=int(input("Enter number"))
a=[]
for i in range(0,n):
  b=int(input())
  a.append(b)
a.sort()
k=int(input("enter k"))
print(a[k-1])
