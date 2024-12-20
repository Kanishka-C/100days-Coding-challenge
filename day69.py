#Multilevel inheritence
class Isosceles:
    def isosceles(self):
        print('I am an isosceles triangle I am a triangle')
class Equilateral(Isosceles):
    def equilateral(self):
        print('I am an equilateral triangle')
eq=Equilateral()
eq.equilateral()
eq.isosceles()