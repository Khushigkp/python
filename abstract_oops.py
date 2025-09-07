# Use ABC module.
#   Create abstract class Animal with abstract method make_sound().
#   Create class Lion that inherits and implements make_sound() with “Roar”.
#   Create object and call the method.
from abc import ABC, abstractmethod
class Animal(ABC):
     @abstractmethod
     def make_sound(self):
      pass
class Lion(Animal):
     def make_sound(self):
      print("Roar")
l=Lion()
l.make_sound()
