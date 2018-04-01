import math
a,b=map(int,input().split(' '))
n=a*b
if(math.sqrt(n)==int(math.sqrt(n))):
  print("YES")
else:
  print("NO")
