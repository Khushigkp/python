# Create a base class Employee with attribute name.
#   Create a child class Manager that adds attribute team_size.
#   Create an object of Manager and print both name and team size.
class Employee:
     def __init__(self,name):
        self.name=name
class Manager(Employee):
      def __init__(self,name,team_size):
           super().__init__(name)
           self.team_size=team_size
m=Manager("Khushi",6)
print(m.name)
print(m.team_size)
