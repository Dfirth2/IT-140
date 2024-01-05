# Dayne Firth II
# commands and Constants
import time

delay = 0.5
DIRECTIONS = ['North', 'South', 'East', 'West']
EXIT_COMMAND = "Exit"
VALID_INPUTS = DIRECTIONS + [EXIT_COMMAND]
INVALID_DIRECTION = "That is not a valid direction. You need to enter one of: " + \
                    str(VALID_INPUTS) + "."
CANNOT_GO_THAT_WAY = "You can't go that way Dumb Dumb! There is a wall there!!"
GAME_OVER = "Thank you for playing!"
EXIT_ROOM = "exit"
def intro():
    # intro
    print("                      Sneezy and the Cat Napper")
    print("Sneezy, The Cat Warrior from Legend, has woken up in a strange facility.")
    print("The Great Cat Catcher Timothy must have gotten the slip on him when he was")
    print("sneezing at the river last night and he must have hit him over the head with something!")
    print("Sneezy must escape from this place. To escape and get past Timothy he needs to unlock")
    print("the front door with 5 different keys and must also get something to reach the locks.")
    print(
        "There are 5 different locks with different shapes on them: a moon, star, triangle, circle, and a square.")
    print("All the while avoiding going into Timothy’s room while he sleeps.")
    time.sleep(delay * 7)

intro()

start = input('Would you like to help Sneezy escape from this place? (Yes or No): ')
if start.lower() == 'yes' or start.lower() == 'y':
    # Continue with the game logic
    print("Great! Let's start the adventure.\n\n")

else:
    print("Maybe next time. " + GAME_OVER)
    exit()
items = {"Moon Key, Square Key, Circle Key, Triangle Key, Star Key, Step Stool"}
rooms = {
    'Front Door': {'South': 'Holding Area'},
    'The Holding Area': {'North': 'Front Door', 'East': 'The Net Closet', 'South': 'Main Hall'},  #Start Here
    'The Net Closet': {'West': 'The Holding Area'},
    'Main Hall': {'North': 'The Holding Area', 'East': 'Kitchen', 'South': '2nd Floor', 'West': 'Timothy\'s Room'},
    'Kitchen': {'East': 'East Tower', 'West': 'Main Hall', 'Item': 'Moon Key'},
    'East Tower': {'West': 'Kitchen', 'Item': 'Square Key'},
    'Timothy\'s Room': {'East': 'Main Hall'},  #villian
    '2nd Floor': {'North': 'Main Hall', 'East': 'War Room', 'West': 'Observatory'},
    'War Room': {'East': 'The Pound', 'West': '2nd Floor', 'Item': 'Circle Key'},
    'The Pound': {'West': 'War Room', 'Item': 'Triangle Key'},
    'Observatory': {'East': '2nd Floor', 'South': 'Broom Closet', 'Item': 'Star Key'},
    'Broom Closet': {'North': 'Observatory', 'Item': 'Step Stool'},
}


def main(user_input: str):
    global current_room
    next_room = current_room
    err_msg = ''
    # Check if the user wants to exit
    if user_input.lower() == EXIT_COMMAND.lower():
        return EXIT_ROOM, GAME_OVER

    # Check if the user input is a valid direction
    if user_input.lower() not in map(str.lower, DIRECTIONS):
        err_msg = INVALID_DIRECTION
        return next_room, err_msg

    # Check if the direction is valid for the current room
    next_room_candidate = rooms[current_room].get(user_input.capitalize())
    if next_room_candidate is None:
        err_msg = CANNOT_GO_THAT_WAY
        return next_room, err_msg

    # Update the current room if the direction is valid
    current_room = next_room_candidate

    return current_room, err_msg


# Set the starting room
STARTING_ROOM = 'The Holding Area'
inventory = []   #sets inventory to blank
current_room = STARTING_ROOM
timthoy = 0

#Current location and inventory
def current_location():
    print('You are in the {}'.format(current_room))
    print('Inventory:', inventory)
# Get the item and addes it to the your inventory
def get_item():
    if 'Item' in rooms[current_room]:
        if rooms[current_room]['Item'] != 'none':
            inventory.append(rooms[current_room]['Item'])
            print("Sneezy has acquired: ", rooms[current_room]['Item'])
            rooms[current_room]['Item'] = 'none'
        else:
            print("There isn't anything in here!")
    else:
        print("There isn't anything in here!")


while True:
    current_location()
    get_item()
    user_input = input('Which Direction would you like to go or Do you want to exit?')
    time.sleep(delay)
    current_room, err_msg = main(user_input)
    if current_room == 'Front Door':
            # winning case
        if len(inventory) == 6:
            print('Sneezy is free, he has escaped from Timothy again!')
            print('Thank you for playing!')
            exit()

        else:
            print('Oh no Sneezy is still missing some items to unlock the Front Door')
            print('Sneezy has collected: ' + ', '.join(inventory) + '.')
            print(' Lets continue Searching this place!')
            current_room = STARTING_ROOM
    if current_room == 'Timothy\'s Room':
        if timthoy == 0:
            print('Sneezy has stumbled into Timothy\'s room.')
            print('Sneezy needs to get out of here before he wakes up')
            timthoy += 1
            current_room = 'Main Hall'
        elif timthoy == 1:
            print('Sneezy has stumbpled on Timothy\'s room again!')
            time.sleep(delay)
            print('Timothy has woken up and grabbed Sneezy...  Everything goes black...')
            inventory.clear()
            current_room = STARTING_ROOM
            time.sleep(delay *2)
            print('Sneezy has awoken back in the holding area and has lost everything.')
            print('He is going to have to find everything again.')

    if err_msg:
        print(err_msg)

    if current_room == EXIT_ROOM:
        break