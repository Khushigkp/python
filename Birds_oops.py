# Create two classes: Parrot and Penguin.
#   Both should have a method fly():
#   - Parrot says: "Parrot can fly."
#   - Penguin says: "Penguin cannot fly."
#   Write a function test_fly(bird) that takes any object and calls fly() on it.
class Parrot:
    def fly(self):
        print("Parrot can fly.")
    
class Penguin:
     def fly(self):
         print("Penguin cannot fly.");
         
def test_fly(bird):
    bird.fly()
p1=Parrot()
p2=Penguin();
test_fly(p1)
test_fly(p2)

