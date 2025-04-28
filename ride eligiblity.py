''' You are at an amusement park. The ride eligibility is based on height and age. Write a Python control flow code to check if a person can ride.
If the person is under 12 years old, they must be at least 120 cm tall to ride.
If the person is 12 to 18 years old, they can ride if they are at least 110 cm tall.
If the person is older than 18, they can ride regardless of height.
'''

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
