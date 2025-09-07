# Create a class Vehicle with method start().
#   Create a class Bike that inherits from Vehicle and has its own method ride().
#   Create an object of Bike and call both methods.
class Vehicle:
  def start(self):
      print("Vehicle start")
class Bike(Vehicle):
     def ride(self):
         print("Bike riding")
b = Bike()
b.start()
b.ride()
