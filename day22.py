#A number as a sum of two prime numbers
import math
def isprime(x):
    count=0
    for i in range(1,int(math.sqrt(x)+1)):
        if x%i==0:
            count+=1
            if(x //i != i):
                count+=1
    if count==2:
        return True
    else:
        return False
num=int(input('Enter a number : '))
for i in range (2,num):
    if isprime(i) and isprime(num-i):
        print(num,'can be expressed as the sum of ',i,' and ',num-i)
        exit(0)
print(num,'cannot be expressed as sum of two primes')