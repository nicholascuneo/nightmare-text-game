def intro():
    print("\nTITLE")
    print("--------------------")
    print("Oogie Boogie is up to his old tricks again, planning to turn the holidays upside down.\n"
          "As Jack Skellington, you must stop him before Christmas is ruined. With the help of your\n"
          "loyal dog, Zero, you'll need to gather 6 items scattered across Halloween Town to help you\n"
          "in your final battle with Boogie. Should you enter Boogie's Lair before collecting all items,\n"
          "Boogie will get the best of you and Christmas will be ruined!\n"
          "--------------------\n")

def instructions():
    print("Directions:\n"
    "To move rooms, type 'go [direction]' (eg. go North, go East..).\n"
    "To add an item to your inventory, type 'get [item name]'.\n"
    #"To exit game, type Exit.\n"
    "To get help, type Help.\n"
    "--------------------")

def status(room, items):
    #FIXME add if statement for grammar
    print("\nYou are in {}.".format(room))
    print("Inventory: {}".format(items))
    print("--------------------")

def main():
    rooms = {
        "Town Hall": {'North': "Mayor's Office", 'South': 'Pumpkin Patch', 'West': "Sally's Sewing Room",
                      'East': "Boogie's Trap Room"},
        "Boogie's Trap Room": {'North': "Boogie's Lair", 'West': 'Town Hall', 'item': 'Lucky Dice'},
        "Boogie's Lair": {'South': "Boogie's Trap Room", 'item': 'Oogie Boogie'},
        "Cemetery": {'West': 'Pumpkin Patch', 'item': 'Nightshade'},
        "Dr. Finkelstein's Lab": {'South': "Sally's Sewing Room", 'East': "Mayor's Office", 'item': 'Scalpel'},
        "Lock, Shock, and Barrel's Treehouse": {'West': "Mayor's Office", 'item': 'Trick-or-Treat bag'},
        "Mayor's Office": {'East': "Lock, Shock, and Barrel's Treehouse", 'West': "Dr. Finkelstein's Lab",
                           'South': 'Town Hall', 'item': 'Cursed Mask'},
        "Pumpkin Patch": {'East': 'Cemetery', 'North': 'Town Hall', 'item': 'Glowing Pumpkin'},
        "Sally's Sewing Room": {'East': 'Town Hall', 'North': "Dr. Finkelstein's Lab", 'item': 'Magic Thread'}
    }

    currentRoom = "Town Hall"
    inventory = []

    intro()
    instructions()

    while currentRoom != "Boogie's Lair":
        status(currentRoom, inventory)
        move = input("Enter your move: ").title().strip()

        if move == 'Help':
            intro()

        elif move.startswith('Go'):
            parts = move.split()
            if len(parts) > 1:
                direction = parts[1]
                if direction in rooms[currentRoom]:
                    currentRoom = rooms[currentRoom][direction]
                else:
                    print("\n*** You can't go that way! ***")
            else:
                print("\n*** Please specify direction. ***")



main()




