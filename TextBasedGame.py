# Define function to share story with user
def intro():
    print("\nOOGIE BOOGIE's REVENGE\n"
    "--------------------\n"
    "Oogie Boogie is up to his old tricks again, planning to turn the holidays upside down.\n"
    "As Jack Skellington, you must stop him before Christmas is ruined. With the help of your\n"
    "loyal dog, Zero, you'll need to gather 7 items scattered across Halloween Town to help you\n"
    "in your final battle with Boogie. Should you enter Boogie's Lair before collecting all items,\n"
    "Boogie will get the best of you and Christmas will be ruined!\n"
    "--------------------")

# Function to print the move instructions
def show_instructions():
    print("\nDirections:\n"
    "--------------------\n"
    "Collect all 7 items before facing Boogie.\n"
    "To move rooms, type 'go [direction]' (eg. go North, go East..).\n"
    "To add an item to your inventory, type 'get [item name]'.\n"
    "To get help, type Help.\n"
    "To quit game, type Quit.\n"
    "--------------------")

# Define function to show status of player
def show_status(room, items, dict_rooms):
    # List of rooms to determine proper grammar of status statement
    rooms_grammar = ["Town Hall", "Cemetery", "Mayor's Office", "Pumpkin Patch"]

    # Output current room
    if room in rooms_grammar:
        print("\nYou are in the {}.".format(room))
    else:
        print("\nYou are in {}.".format(room))

    # Check if current room has an 'item' key
    if dict_rooms[room].get('item') is not None:
        print("\nYou see a {}".format(dict_rooms[room].get('item'))) # If item exists in room, output to player

    # Output player inventory
    if len(items) == 1: # Account for singular item
        print("Inventory ({} item): {}".format(len(items), items)) # Player's inventory
    else:
        print("Inventory ({} items): {}".format(len(items), items))

    print("--------------------")
    move = input("Enter your move: ").title().strip()  # Get move command from player

    return move # Return the move command from player

# Main game function
def main():
    # Set dictionary of rooms, directions, and items
    rooms = {
        "Town Hall": {'North': "Mayor's Office", 'South': 'Pumpkin Patch', 'West': "Sally's Sewing Room",
                      'East': "Boogie's Trap Room"},
        "Boogie's Trap Room": {'North': "Boogie's Lair", 'West': 'Town Hall', 'item': 'Lucky Dice'},
        "Boogie's Lair": {'South': "Boogie's Trap Room", 'item': 'Oogie Boogie'},
        "Cemetery": {'West': 'Pumpkin Patch', 'item': 'Nightshade'},
        "Dr. Finkelstein's Lab": {'South': "Sally's Sewing Room", 'East': "Mayor's Office", 'item': 'Scalpel'},
        "Lock, Shock, and Barrel's Treehouse": {'West': "Mayor's Office", 'item': 'Trick Or Treat Bag'},
        "Mayor's Office": {'East': "Lock, Shock, and Barrel's Treehouse", 'West': "Dr. Finkelstein's Lab",
                           'South': 'Town Hall', 'item': 'Cursed Mask'},
        "Pumpkin Patch": {'East': 'Cemetery', 'North': 'Town Hall', 'item': 'Glowing Pumpkin'},
        "Sally's Sewing Room": {'East': 'Town Hall', 'North': "Dr. Finkelstein's Lab", 'item': 'Magic Thread'}
    }

    # Set player in starting room and initiate player inventory list
    currentRoom = "Town Hall"
    inventory = []

    # Call intro and instruction functions
    intro()
    show_instructions()

    # Main game loop
    while currentRoom != "Boogie's Lair":
        move = show_status(currentRoom, inventory, rooms) # Capture returned move from calling show status function

        if move == 'Help': # Print instructions if 'help' is input as player move
            show_instructions()

        elif move == 'Quit':
            user_quit = input("Are you sure? (y/n): ").lower().strip() # Confirm if player wants to quit
            if user_quit == 'y':
                print("\nThank you for playing. Goodbye!")
                break # Exit main loop and end game
            elif user_quit == 'n':
                print("\nContinuing your quest...") # Continue game loop
            else:
                print("\nInvalid response. Please type 'y' for yes or 'n' for no.") # Handles invalid command

        # Check if move starts with 'Go' which indicates move to another room
        elif move.startswith('Go'):
            parts = move.split() # Parse valid directional move command into list
            if len(parts) > 1: # Ensures direction is provided in command
                direction = parts[1] # Direction assigned to variable
                if direction in rooms[currentRoom]: # Checks if direction matches key in current room nested dictionary
                    currentRoom = rooms[currentRoom][direction] # Move player to new room
                else:
                    cardinal_directions = ["North", "South", "East", "West"] # List of valid cardinal directions

                    if direction not in cardinal_directions: # Check if input direction is valid to determine output
                        print("\n*** Be sure to enter a cardinal direction. ***") # Output if direction is invalid
                    else:
                        print("\n*** You can't go that way! ***") # Output if direction not available for current room
            else:
                if len(parts[0]) > 2: # Checks if player entered 'Go' + 'direction' without a space
                    print("\n*** Invalid command ***")
                else:
                    print("\n*** Please specify direction. ***") # Handles case if player only inputs 'Go'

        # Check if move starts with 'Get' indicating taking an item from room
        elif move.startswith('Get'):
            parts = move.split() # Parse item after 'Get' into list
            if len(parts) > 1: # Ensures item is provided in command
                item = ' '.join(parts[1:])  # Join everything after 'Get' for multi-word items

                # Check if 'item' key exists in current room and if it matches item provided in player command
                if 'item' in rooms[currentRoom] and rooms[currentRoom]['item'] == item:
                    inventory.append(rooms[currentRoom].pop('item')) # Remove item from rooms dict and add to inventory
                    print("\nYou grabbed the {}!".format(item)) # Output when addition to inventory is successful
                else:
                    print("\n*** There is no {} here! ***".format(item)) # Output if item does not exist in current room
            else:
                if len(parts[0]) > 3: # Checks if player input 'get' + 'item' without a space
                    print("\n*** Invalid command ***")
                else:
                    print("\n*** Please specify item. ***") # Handles case if player only inputs 'Get'

        else: # Handles if player inputs invalid command
            print("\n*** Invalid command ***")

    # Win or lose scenarios and outputs when player enters Boogie's Lair
    if currentRoom == "Boogie's Lair":
        if len(inventory) < 7: # Player has not collected all items
            print("\nOh no, Jack Skellington...")
            print("You stumbled into Boogie's Lair without all the items!")
            print("Oogie Boogie towers over you and casts you into a pit of bugs!")
            print("Christmas is ruined. Goodbye.")
        else: # Player collects all items and wins game
            print("\nCongratulations, Jack Skellington!")
            print("You have all the necessary items, and with Zero's help, you defeat Oogie Boogie!")
            print("Christmas is saved! Santa can finally make his deliveries, and all is merry in Halloween Town.")
            print("You are the Pumpkin King!")


main()