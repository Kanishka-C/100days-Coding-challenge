import math
a,b,c=map(int,(input('Enter the values of a, b, c :').split()))
d=math.pow(b,2)-4*a*c
if d==0:
    print("Roots are equal")
    print('Root 1= Root 2=',(-b)/2*a)
elif d<0:
    print("Roots are complex")
else:
    r1=(-b+math.sqrt(d))/2*a
    r2=(-b-math.sqrt(d))/2*a
    print("Root 1=",r1,"Root 2=",r2)
    