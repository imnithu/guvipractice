n=input("Enter a string")
a=[]
for i in n:
  if(i.isdigit()):
    a.append(i)
print("".join(n for n in a))
