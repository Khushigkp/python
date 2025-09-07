# Define a class Book that stores the title and
# author. Add a method display() that prints both.
# Use the method on one object.
class Book:
    def __init__(self):
       self.title ="i will be my best version"
       self.author="khushi"
    def display(self) :
        print("title",self.title)
        print("author" , self.author)
b=Book()
b.display();
