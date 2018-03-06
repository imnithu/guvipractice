a=[]
n=int(input("Enter the number of terms"))
for i in range (0,n):
  b=int(input("Enter the number"))
  a.append(b)
a.sort()
print(a[(n-1)//2])
