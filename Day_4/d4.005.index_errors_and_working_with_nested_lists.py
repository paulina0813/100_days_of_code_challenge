dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches",
               "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches","Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

#nested lists
dirty_dozen_nested = [fruits, vegetables]

#This will print the item in index 2 of the list vegetables (index 1)
print(dirty_dozen_nested[1][2])