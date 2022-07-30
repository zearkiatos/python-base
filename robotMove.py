NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'

LEFT = 'L'
RIGHT = 'R'
HALF = 'H'
KEEP = '.'


def robotMove(orientation: str, turn1: str, turn2: str, turn3: str) -> str:
    orientation
    position = turnTo(turn1, orientation)
    position = turnTo(turn2, position)
    position = turnTo(turn3, position)

    return position


def turnTo(turn: str, ori: str) -> str:
    orientation = ''
    if (turn == LEFT):
        orientation = turnLeft(ori)
    if (turn == RIGHT):
        orientation = turnRight(ori)
    if (turn == HALF):
        orientation = turnHalf(ori)
    if (turn == KEEP):
        orientation = turnKeep(ori)
    return orientation


def turnLeft(orientation: str) -> str:
    position = ''
    if (orientation == NORTH):
        position = WEST
    elif (orientation == WEST):
        position = SOUTH
    elif (orientation == SOUTH):
        position = EAST
    elif (orientation == EAST):
        position = NORTH
    return position


def turnHalf(orientation: str) -> str:
    position = ''
    if (orientation == NORTH):
        position = SOUTH
    elif (orientation == SOUTH):
        position = NORTH
    elif (orientation == EAST):
        position = WEST
    elif (orientation == WEST):
        position = EAST
    return position


def turnRight(orientation: str) -> str:
    position = ''
    if (orientation == NORTH):
        position = EAST
    elif (orientation == EAST):
        position = SOUTH
    elif (orientation == SOUTH):
        position = WEST
    elif (orientation == WEST):
        position = NORTH
    return position


def turnKeep(orientation: str) -> str:
    return orientation


print(robotMove(NORTH, LEFT, HALF, LEFT))
