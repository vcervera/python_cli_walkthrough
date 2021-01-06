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
next_id = 0
items = [1,2,3]
# TODO Make a menu print out showing options
def menu():

    print ("""
1.List all items
2.add new item
3.update exisitng item
4.delete item (by item id)
5.Exit

""")

# List all items

def list_items():
    for item in items:
        print(item)
    print("in list itme function")

# #add new item

def new_item():
    global next_id
    name = input("Name:")
    cond = input("Conditions: ")
    item_id = next_id
    next_id += 1


# 3.update exisitng item

def update_existing(itemId):
    pass


# 4.delete item (by item id)

def delete_item(itemId):
    pass


# Make the menu questions that grab the data

while True:
    menu()
    choice = input(">")

    if choice == "1":
        list_items()
        #pass
    elif choice ==  "2":
        new_item()
    elif choice ==  "3":
        pass
    elif choice ==  "4":
        pass
    #Exit
    if choice ==  "5":
        exit()
    else:
        input("Invalid Input, give a number\n(Press enter to try agian)")

# Make the File saving stuff
# # try:
    #     choice = int(input("> "))
    # except Exception:
    #     input("Invalid Input, give a number\n(Press enter to try agian)")
        # continue