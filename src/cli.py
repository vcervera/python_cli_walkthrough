
from models.item import Item # And Import Statement to make code from other files available

next_id = 0
items = [] # this will be used to store items 
# TODO Make a menu print out showing options
def menu(): # prints the menu option for the user
    print ("""
1.List all items
2.add new item
3.update exisitng item
4.delete item (by item id)
5.Exit
""")

# List all items

def list_items(): # Writes all items to the terminal
    for item in items:
        print(item)

#add new item

def new_item(): # gets user input for all need fields for an Item
    global next_id # allows us access to the next_id number

    name = input("Name:")
    cond = input("Condition: ")
    item_id = next_id # uses the global counter to give a unique id to each item
    next_id += 1 # updates id with new value so next one is 1 more

# This is the class -> Item from the other file we imported 
    tmp = Item(item_id, name, cond) # Builds an item/stores it in tmp 
    items.append(tmp) # adds item to global items array

# 3.update exisitng item

def update_existing():
    if not items:
        print("You have not items to update")
        return
    list_items()
    try:
        item_id_to_update = int(input("What is the item you wish to update\n>"))
    except Exception:
        print("not a valid number")
        return
    for item in items:

        if item.item_id == item_id_to_update:
            item.name = input("Name: ")
            item.condition =input("Condition: ") 
           
            break
    #if found_item:   
    else:
        print("We didn't find a match")


# 4.delete item (by item id)

def delete_item():
    print("inside del item")
    if not items:
        print("You have no items to delete")
        return
    list_items()
    try:
        item_id_to_delete = int(input("What is the item you wish to update\n>"))
    except Exception:
        print("not a valid number")
        return

    for index, item in enumerate(items):
        if item.item_id == item_id_to_delete:
            index_to_remove = index
            break
        else:
            print("We don't find a match")
            return
        removed_item = items,pop(index_to_remove)
        print(f"Found: \n {items.pop(index_to_remove)}")

def main():  # Starts the Program off, holds the loop until exit.
    while True:
        menu()  # Prints the Options to the Terminal
        choice = input("> ")  # Takes use choice

        # The Conditional Options: hands off the work to the functions above.
        if choice == "1": 
            list_items() 
        elif choice == "2":
            new_item()
        elif choice == "3":
            update_existing()
        elif choice == "4":
            delete_item()
        elif choice == "5": # Exit
            exit()
        else:  # User gave us bad input we let them know then loop again.
            input("Invalid Input!\n(Press Enter to try again)")

# Make the File Saving stuff

if __name__ == "__main__":
    main()
