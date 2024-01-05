# Dayne Firth II
# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}
# commands and Constants
DIRECTIONS = ['North', 'South', 'East', 'West']
EXIT_COMMAND = "Exit"
VALID_INPUTS = DIRECTIONS + [EXIT_COMMAND]
INVALID_DIRECTION = "That is not a valid direction. You need to enter one of: " + \
                    str(VALID_INPUTS) + "."
CANNOT_GO_THAT_WAY = "You can't go that way Dumb Dumb! There is a wall there!!"
GAME_OVER = "THANK YOU FOR PLAYING!!"
EXIT_ROOM = "exit"

# Set the starting room
STARTING_ROOM = 'Great Hall'
current_room = STARTING_ROOM


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


while True:
    print('You are current in the', current_room + '.')
    user_input = input('Which Direction would you like to go or Do you want to exit?')

    current_room, err_msg = main(user_input)

    if err_msg:
        print(err_msg)

    if current_room == EXIT_ROOM:
        break