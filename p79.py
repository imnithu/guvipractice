n=int(input("Enter the n"))
a=[]
for i in range(0,n):
  b=int(input())
  a.append(b)
a.sort()
print(a[n-1]-a[0])
