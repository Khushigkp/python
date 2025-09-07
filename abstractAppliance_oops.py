# Create an abstract class Appliance with an abstract method turn_on().
#   Make two classes: Fan and Bulb that implement turn_on() differently.
#   Call both methods and print the output.
from abc import  ABC , abstractmethod
#from abc import ABC, abstractmethod
class Appliance (ABC):
    @abstractmethod 
    def turn_on(self):
        pass
class Fan :
    def turn_on(self):
        print("Fan turn on")
class Bulb:
    def turn_on(self):
        print("Bulb turn on")
        
f=Fan()
b=Bulb()
f.turn_on()
b.turn_on()
