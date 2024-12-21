#Multilevel inheritence
class Isosceles:
    def isosceles(self):
        print('I am an isosceles triangle')
class Equilateral(Isosceles):
    def equilateral(self):
        print('I am an equilateral triangle')
class C (Equilateral):
    def display(self):
        print('I am a triangle')
c=C()
c.equilateral()
c.isosceles()
c.display()
