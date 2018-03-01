n=int(input("Enter the minutes to convert")) 
a='{:02d}:{:02d}'.format(*divmod(n, 60))
print(a)
