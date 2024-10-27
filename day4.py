n=int(input('Enter a number : '))
if n==0:
    print("Neither positive nor negative")
elif n>0:
    print("Positive number")
else:
    print("Negative number")

num=int(input('Enter a number : '))
print("Positive number"if num>0 else("Negative number" if num<0 else "Neither positive nor negative"))