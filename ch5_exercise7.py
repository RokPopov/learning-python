"""Grocery List
Try creating a Python program that will capture and display a person’s grocery shopping list. Make it so the program
will continually prompt the user for another item until the point where they enter a blank item. After all the items
have been entered, try displaying the shopping list back to the user."""

grocery_list = []
end_of_list = False
while not end_of_list:
    list_item = input("Enter an item for your grocery list and press ENTER. You end the list by adding an empty item: ")
    if len(list_item) == 0:
        end_of_list = True
    else:
        grocery_list.append(list_item)
        print("You added an item to your grocery list! Well done!")

print("Your Grocery List:")
print()
for i in grocery_list:
    print(i)