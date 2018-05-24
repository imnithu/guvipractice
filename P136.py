b=int(input("Enter the array size"))
a=[]
for i in range(0,b):
  c=(input("Enter the number"))
  a.append(c)
k=input("Enter any Number to be Checked")
if k in a:
  print("yes", a.count(k))
else:
  print("no")
