
n,k=map(int,input("Enter the values of n,k").split(" "))

a=[]

for i in range(0,n):

  b=int(input())

  a.append(b)

a.sort()

if k in a:

  print("yes")

else:

  print("no")
