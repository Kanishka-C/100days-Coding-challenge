x,y = map(int,(input('Enter x and y coordinates : ').split()))
if x>0 and y>0:
    print('This point lies in first quadrant.')
elif x>0 and y<0:
    print('This point lies in fourth quadrant.')
elif x<0 and y>0:
    print('This point lies in second quadrant.')
elif x<0 and y<0:
    print('This point lies in third quadrant.')
else:
    print('This point lies in the axis')