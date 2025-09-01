available = {"salt", "sugar", "flour", "eggs", "milk"}
recipe = {"flour", "eggs", "butter", "sugar"}
print(available|recipe)
print(available&recipe)
print(available-recipe)
print(recipe-available)
