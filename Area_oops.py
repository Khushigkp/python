#  Create a class Shape with method area().
#   Then make two classes:
#   - Rectangle with width and height
#   - Circle with radius
#   Both should override area() to give correct output. Call area() for both objects.
class Shape:
    def area(self):
        print("area")
class Rectangle(Shape):
     def __init__(self, width , height):
       self.width=width
       self.height=height
     def area(self):
         return self.width *self.height
class  Circle(Shape):
      def __init__(self,radius):
         self.radius=radius
      def area(self):
          return 3.14*self.radius*self.radius
r=Rectangle(2,3)
c=Circle(2)
print(r.area())
print(c.area())


