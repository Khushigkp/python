students = {"Ram":90 ,"Shayam": 85 , "Krishna": 86 , "Pawan":80}
print(type(students));
##Add a new student 'Alice' with the average score of all the original 4 students
avg = sum(students.values())/len(students);
students["Alice"]=avg
print(students);
##Remove the student who has the lowest score using
lowest_marks = min(students , key=students.get);
del students[lowest_marks];
print(students);
## Remove the student who has the lowest score using
students.popitem()
print(students);
##Remove the last added student and store their score in a new key called 'Archived'
achieved = students.popitem()
print(achieved)
## Delete the first key 
##firstKey=students.pop("Ram")
first_key=next(iter(students))
##print(first_key)
print(students);



