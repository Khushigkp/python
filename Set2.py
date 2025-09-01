students = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]
python_enrolled = ["Alice", "Charlie", "Eva"]
ml_enrolled = ["Bob", "Charlie", "David", "Eva"]
print(type(students))
print(type(python_enrolled))
print(type(ml_enrolled))
students = set(students);
python_enrolled = set(python_enrolled);
ml_enrolled = set(ml_enrolled);
print(type(students))
print(type(python_enrolled))
print(type(ml_enrolled))
##for x in students:
##if(len(x)>4):
## print(x)
### creating a set and string the name whose letter are greater then 4
longName={ x for x in students if(len(x)>4)}
print(longName)
print(type(students))
### printing the students who enrolled in both python as well ml_enrolled
print(python_enrolled & ml_enrolled)
print(ml_enrolled)
##Add "George" to the Python course set
students.add("George")
print(students)
##Remove "Eva" from ML course using discard.
ml_enrolled.discard("Eva")
print(ml_enrolled)
##Try removing "Zara" from Python course using remove and handle the error gracefully.
try:
  python_enrolled.remove("Zara") 
except KeyError:
     print("we cant use remove if zara will not be presnt in set then it will give you error use discard")
## Update the ML course set with a 
new_batch ={"Helen", "Ian"}
ml_enrolled.update(new_batch)
print(ml_enrolled)
## Check if all Python students are part of the general students list
if students.issubset(python_enrolled):
  print("yes")
else:
   print("No")  
##Create a frozenset from the intersection of both courses and show its
##hashability using it as a dictionary key.
both_curses_common = python_enrolled & ml_enrolled
forzen_both_curses_common = frozenset(both_curses_common)
print(forzen_both_curses_common)
course_dict = {forzen_both_curses_common: "Common students in both courses"}
print(course_dict)
print(course_dict[forzen_both_curses_common])

    





 
