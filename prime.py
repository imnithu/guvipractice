n=int(input("enter a number"))
if(n==2):
  print("It is a Prime number")
elif n > 2:
  for i in range(2,n):
    if (n % i) == 0:
      print("It is not a prime number")
      break
    else:
      print("It is a prime number")
      break
else:
  print("It is not a prime number")
