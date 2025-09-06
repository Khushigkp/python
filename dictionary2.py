# Create a dictionary named inventory with 5 products as keys and their quantities as values 
# (all quantities should be positive integers).
inventory ={"lamp":10,"bulb":5,"wire":2,"switch":15,"phone":20 }
# Add a new product called 'BackupItem' whose quantity is the sum of the quantities of the first two products.
q = inventory["lamp"]+inventory["bulb"]
inventory["BackupItem"]=q
print(inventory);
# identify the product with the maximum quantity and remove it from the dictionary.
high= max(inventory , key=inventory.get)
inventory.pop(high)
print(inventory)
# Move the most recently added product and its quantity into a new key called 'LastRemoved' and
# remove it from its original place.
# LastRemoved = inventory.items();
# inventory.pop(LastRemoved)
last_key , last_value = list(inventory.items())[-1]
inventory.pop(last_key)
print(inventory)
# Remove the second product (in insertion order) from the dictionary.
second_key , second_value = list(inventory.items())[1]
inventory.pop(second_key)
print(inventory)
# If only two or fewer products remain, remove everything from the dictionary.
if len(inventory) <=3:
    inventory.clear()
print(inventory)
#Finally, if the dictionary becomes empty, add two new products with quantity 0, and print only the product names.
if len(inventory) == 0 :
    inventory.update({"lmno":0 })
    inventory.update({"ABC":0 })
print(inventory)


