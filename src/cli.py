
from models.item import Item # And Import Statement to make code from other files available
import csv

next_id = 0
items = [] # this will be used to store items 
# TODO Make a menu print out showing options
def menu(): # prints the menu option for the user
    print ("""
1.List all items
2.Add new item
3.Update exisitng item
4.Delete item (by item id)
5.Exit
""")

# List all items

def list_items(): # Writes all items to the terminal
    """
    1) read the file into Python
    2) Parse the file into usable data
    3) Print out each item in the file
    """
    with open('inventory.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            message = f"ID: { row['id'] }\tName: {row['name'] }\tCondition: { row['condition'] }"
            print(message)

    # for item in items:
    #     print(item)

#add new item

def new_item(): # gets user input for all need fields for an Item

    """
    TODO
    1) Open and parse the file into CSV
    2) Detect what the next id will  be
    3) Prompt the user for new item data (name, conditon)
    4) Add this item to to the inventory.csv file
    """
    with open('inventory.csv', 'r+') as file:
        current_items = list(csv.DictReader(file))
        try:
            last_id = int(current_items[-1]['id'])
        except IndexError:
            last_id = -1

    with open('inventory.csv', 'a+', newline='') as file:
        name = input('Name: > ')
        condition = input('Condition: > ')
        item = {
            "id": last_id + 1,
            "name": name,
            "condition": condition
        }
        writer = csv.DictWriter(file, ["id", "name", "condition"])
        if last_id == -1:
            writer.writeheader()
        writer.writerow(item)
    

#     global next_id # allows us access to the next_id number

#     name = input("Name:")
#     cond = input("Condition: ")
#     item_id = next_id # uses the global counter to give a unique id to each item
#     next_id += 1 # updates id with new value so next one is 1 more

# # This is the class -> Item from the other file we imported 
#     tmp = Item(item_id, name, cond) # Builds an item/stores it in tmp 
#     items.append(tmp) # adds item to global items array

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
        removed_item = items.pop(index_to_remove)
        print(f"Found: \n {items.pop(index_to_remove)}")

def main():  # Starts the Program off, holds the loop until exit.
    # detect if the invertory.csv file exists. Create if not
    open('inventory.csv', 'a+').close()
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
