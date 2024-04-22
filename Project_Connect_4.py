from typing import List, Union


def checkWinningState(field: List[List[Union[int, str]]]):
    """
    Check if there is a winning state in the game field.
    Args:
        field (list[list[int | str]]): The game field represented as a 2D list.
    Returns:
        bool: True if there is a winning state, False otherwise.
    """

    def check_field_limit(i: int, j: int) -> bool:
        return 0 <= i < len(field) and 0 <= j < len(field[0])

    def check_right(field: List[List[Union[int, str]]], i: int, j: int) -> bool:
        for k in range(4):
            if not check_field_limit(i, j + k):
                return False
            if field[i][j + k] != field[i][j]:
                return False
        return True

    def check_down(field: List[List[Union[int, str]]], i: int, j: int) -> bool:
        for k in range(4):
            if not check_field_limit(i + k, j):
                return False
            if field[i + k][j] != field[i][j]:
                return False
        return True

    def check_diagonal(field: List[List[Union[int, str]]], i: int, j: int) -> bool:
        for k in range(4):
            if not check_field_limit(i + k, j + k):
                return False
            if field[i + k][j + k] != field[i][j]:
                return False
        return True

    def check_diagonal2(field: List[List[Union[int, str]]], i: int, j: int) -> bool:
        for k in range(4):
            if not check_field_limit(i + k, j - k):
                return False
            if field[i + k][j - k] != field[i][j]:
                return False
        return True

    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == "*":
                continue
            if (
                    check_right(field, i, j)
                    or check_down(field, i, j)
                    or check_diagonal(field, i, j)
                    or check_diagonal2(field, i, j)
            ):
                return True
    return False


def generateField(nrow, ncol):
    field = []
    for row in range(nrow):
        temp_list = []
        for cln in range(ncol):
            temp_list.append("*")
        field.append(temp_list)
    return field


def drawField(field):
    for row in field:
        print(row)


def doMove(player, field):
    column = int(input(f"Please input the column 0-{len(field) - 1}: "))
    while column > len(field):
        column = int(input(f"Please input the column 0-{len(field) - 1}: "))
    coordinate = checkEmptySlot(column, field)
    if coordinate >= 0:
        if player == 0:
            field[coordinate][column] = "R"
        else:
            field[coordinate][column] = "Y"
    else:
        print("Column full.")
        doMove(player, field)


def check_board(field):
    Board_full = True
    for row in field:
        for col in row:
            if col == "*":
                Board_full = False
                break
            if not Board_full:
                break
    return Board_full


def checkEmptySlot(col, field):
    noEmptySlot = -1

    for i in range(len(field) - 1, -1, -1):
        if field[i][col] == "*":
            noEmptySlot = i
            break

    return noEmptySlot


def startGame(field, nrow, ncol):
    player = bool(0)
    win = False
    winner_ = -1
    print("* * * * C O N N E C T 4 * * * *")
    print()
    print("Player-0 plays Red. Player-1 plays Yellow. \n Red starts")
    print()

    while not win and not check_board(field):
        drawField(field)
        doMove(player, field)
        win = checkWinningState(field)
        if not win:
            player = not player
        else:
            winner_ = player
            break
    return winner_


print()
print("Welcome to Connect-four! Please choose number of rows and columns for your board:")
r = int(input("Rows: "))
c = int(input("Columns: "))
print()
f = generateField(r, c)
winner = startGame(f, r, c)

for rows in f:
    print(rows)

if winner == 0:
    print("WINNER: Red")
elif winner == 1:
    print("WINNER: Yellow")
else:
    print("DRAW")