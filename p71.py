n=int(input("Enter a number"))
a=[]
for i in range(0,n):
  b=int(input())
  a.append(b)
for i in range(1,n):
  if(a[i]>a[i-1]):
    print(a[i])
  else:
print(a[i-1])
