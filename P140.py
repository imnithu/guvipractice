s=input("Enter a string")
a=len(s)
n=0
for i in s:
  if (i=="a" or i=="b"):
    n=n+1
if(n==a):
 print("yes")
else:
  print("no")
