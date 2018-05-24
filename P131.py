a=map(int,input("Enter any number : "))
l=[]
b=[]
for i in a:
  l.append(i)
for j in l:
  if (int(j) % 2)!=0:
   b.append(j)
c=sum(b)
if(c%2==0):
  print("E")
else:
  print("O")
