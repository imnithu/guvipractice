S=input("Enter a string")
n=['a','e','i','o','u']
for i in S:
  if(i in n):
    print("Yes")
    break
else:
  print("No")
