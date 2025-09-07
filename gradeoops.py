# Create a class Student with:
#   - Public attribute: name
#   - Private attribute: __grade
#   - Methods to set and get the grade (with checks that grade is A, B, or C only)
#   Test the class with an invalid grade as well.
# class Student:
class Student:
    def __init__(self,name,grade):
       self.name=name
       self.__grade = None
       self.Set_grade(grade)
    def Set_grade(self,grade):
         
         if grade == "A" or grade == "B"or grade == "C":
              self.__grade=grade
         else:
             print("invalid grade")
    def get_grade(self):
        return self.__grade
s=Student("khushi","A")
print(s.name)
print(s.get_grade())v
