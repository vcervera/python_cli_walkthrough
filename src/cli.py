"""
Work wants an inventory app that:
    Stores data into a file 
    uses the commad line to list add/update/ delete:
        "items" they have:
            id
            name
            conditions
            bnous: checked in
"""
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
    # print("in list itme function")

# #add new item

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

def update_existing(itemId):
    pass


# 4.delete item (by item id)

def delete_item(itemId):
    pass


# Make the menu questions that grab the data

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
            pass
        elif choice == "4":
            pass
        elif choice == "5": # Exit
            exit()
        else:  # User gave us bad input we let them know then loop again.
            input("Invalid Input!\n(Press Enter to try again)")

# Make the File Saving stuff

if __name__ == "__main__":
    main()


# Make the File saving stuff
# # try:
    #     choice = int(input("> "))
    # except Exception:
    #     input("Invalid Input, give a number\n(Press enter to try agian)")
        # continue