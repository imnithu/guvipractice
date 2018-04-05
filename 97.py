a=int(input("Enter Starting Range"))
b=int(input("Enter Ending Range"))
s=0
for i in range(a,b+1):
  if(i%2!=0):
    s=s+i
print(s)
