class Shape:
    def Area(self):
        area=0
        print("Area of Shape is: ",area)

class Square(Shape):
    def __init__(self, length):
        self.length=length
        print("Length of Square is: ",self.length)
    def area(self):
        A=self.length*self.length
        print("Area is:",A)
        
  
oj1=Shape()
oj1.Area()
oj2=Square(2)
oj2.length
oj2.area()



    