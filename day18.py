div=0
x1,y1,x2,y2=map(int,(input('Enter x1,y1,x2,y2 : ').split()))
if y1!=0 and y2!=0:
    x3=(x1*y2)+(x2*y1)
    y3=y1*y2
    if x3>y3:
        div=y3
    else:
        div=x3
    for i in range(div,0,-1):
        if(x3%i==0) and (y3%i==0):
            x3=x3//i
            y3=y3//i
print('Sum of fractions : ',x3,'/',y3)