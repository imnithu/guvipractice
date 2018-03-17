def lcm(x, y):
   if x > y:
       a = x
   else:
       a = y
   while(True):
       if((a % x == 0) and (a % y == 0)):
           lcm = a
           break
       a += 1

   return lcm
b=int(input("Enter number"))
c=int(input("Enter next number"))
print(lcm(b,c))
