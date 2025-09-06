scores = {"ram":98 ,"shyam":90 ,"arav":100 ,"Das":95 }
print(scores)
avg=sum(scores.values())/len(scores)
scores.update({"alic" : avg})
print(scores)
# scores['ali']=avg
# print(scores)
# Remove the student who has the lowest score using
# a=min(scores.values())
# key=scores.get(a)
key = min(scores, key=scores.get)
scores.pop(key)
print(scores)
# Remove the last added student and store their score in a new key called 'Archived'.
achieved=scores.popitem()
print(scores)
# Delete the first key .
f=next(iter(scores))
scores.pop(f)
print(scores)
# Clear the entire dictionary only if the number of remaining keys is less than 2.
if len(scores)<2:
    scores.clear()
# print(scores)If the dictionary is empty, re-initialize it with any 2 key-value pairs and print only the values using dictionary methods.

if not scores:
    scores={"java":100 , "dsa":100}
    print(scores)




