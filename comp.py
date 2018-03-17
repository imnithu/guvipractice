n=int(input("Enter a number"))
if n==1 or n==0:
  print("Neither prime nor composite")
elif n>1:
  for i in range(2,n):
    if(n%i==0):
      print("Yes")
      break
  else:
      print("No")
