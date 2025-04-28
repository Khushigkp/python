age = int(input("Enter the age: "))
height = int(input("Enter the height: "))

if age == 12 and height >= 120:  
    print("Person can ride")
elif 12 < age < 18 and height >= 110:  
    print("Person can ride")
elif age < 12 and height >= 120: 
    print("Person can ride")
else:
    print("Person cannot ride") 
