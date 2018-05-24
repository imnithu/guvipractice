a=list(input("Enter the numbers"))
b=a[:len(a)//2]
c=a[len(a)//2:]
b.sort()
print('Ascending Order of First Half:',b)
print('Descending Order of Second Half:',sorted(c,reverse=True))
