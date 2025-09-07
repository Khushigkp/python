# Write a class Dog with attributes name and
# breed, set using __init__. Create two objects 
# with different values and print their details.
class Dog:
   def __init__(self , name ,breed):
     self.name = name
     self.breed= breed
d1=Dog("jerry" , "pub")
d2=Dog("micky" , "husky")
print(d1.name)
print(d2.name)
print("Dog 1:", d1.name, "-", d1.breed)
print("dog2:",d2.name , "-" ,d2.breed)
print("Dog 2:", d2.name, "-", d2.breed)
