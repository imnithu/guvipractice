n=int(input("Enter value of N"))
p=[]
for k in range(0,n):
  a=int(input("Enter the numbers :"))
  p.append(a)
b=p[len(p)//2:]
c=p[:len(p)//2]
print(b,c)
f=sum(b)/len(b)
g=sum(c)/len(c)
if f==g:
  print("yes")
else:
  print("no")
