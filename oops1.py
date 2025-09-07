# Create a class Car with two attributes:
#     brand and model. Create an object of the class and 
#     print both attributes.
class Car:
     def __init__(self ,brand , model):
      self.brand= brand
      self.model=model
     
c = Car("maruti" , 123)
print(c.brand);
