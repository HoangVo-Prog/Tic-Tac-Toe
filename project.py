import random


def draw_board(board: list) -> str:
    """
    :param board: a list representing the board
    :return: a string that easier to read and play the game
    """
    string = ""
    for index in range(3):
        string += f"{board[index][0]}|{board[index][1]}|{board[index][2]}\n"
    return string


def is_full(board: list) -> bool:
    """
    :param board: a list representing the board
    :return: bool that regardless of whether the board is full
    """
    for row in range(3):
        for col in range(3):
            if board[row][col].isspace():
                return False
    return True


def check_letter(board: list, position: list, letter: str = " ") -> bool:
    """
    :param board: a list representing the board
    :param position: position that locate the letter
    :param letter: white space | "x" | "o"
    :return: bool that regardless of whether the exact letter is in the position of the list
    """
    return True if board[position[0]][position[1]] == letter else False


def game_over(board: list, letter: str) -> bool:
    """
    :param board: a list representing the board
    :param letter: "x" | "o"
    :return: winning of "x" | "o" or draw condition
    """
    for index in range(3):
        if ((board[index][0] == letter and board[index][1] == letter and board[index][2] == letter) or
                (board[0][index] == letter and board[1][index] == letter and board[2][index] == letter)):
            return True
    if board[0][0] == letter and board[1][1] == letter and board[2][2] == letter:
        return True
    if board[0][2] == letter and board[1][1] == letter and board[2][0] == letter:
        return True
    return False


def move_to_win_and_defense(board: list, letter: str) -> list:
    """
    :param board: a list representing the board
    :param letter: "x" | "o"
    :return: a list of position that the next move can lead computer/human to win
    """
    for row in range(3):
        for col in range(3):
            new_board = [[board[row][col] for col in range(3)] for row in range(3)]
            if check_letter(new_board, [row, col]):
                new_board[row][col] = letter
                if game_over(new_board, letter):
                    return [row, col]


# todo
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print(draw_board(board))  # create and initialize the chess board
    while True:
        letter = input("Choose a letter (x/o) to play: ").casefold().strip()
        if letter in ["x", "o"]:
            human_comp = ["x", "o"] if letter == "x" else ["o", "x"]
            break
    print(f"You play {human_comp[0]} and computer play {human_comp[1]}")
    first_turn = "computer" if random.randint(0, 1) == 0 else "human"
    order = 1
    print(f"{first_turn.title()} goes first")
    while True:
        """
            first we need to separate into 2 case that human goes first or computer go first
            human goes first: lead to draw or the win for computer.
        """
        if first_turn == "human":
            match order:
                case 2:
                    """ if human is "x" then computer is "o", there are two case
                                        [["x", " ", " "],
                                         [" ", "o", " "],
                                         [" ", " ", " "]]
                                        and
                                        [["o", " ", " "],
                                         [" ", "x", " "],
                                         [" ", " ", " "]]
                                        """
                    if check_letter(board, [1, 1], human_comp[0]):
                        board[0][0] = human_comp[1]
                    else:
                        board[1][1] = human_comp[1]
                case 4:
                    """ There are two big cases that:
                    1st: automatic handle when human is about to win, for instance:
                                        [["x", " ", " "],
                                         ["o", "o", " "],
                                         ["x", " ", " "]]
                        or
                                        [["o", "o", " "],
                                         [" ", "x", " "],
                                         [" ", "x", " "]]
                    2nd: the other is the case that human not make any move that
                     can be win in the next move if it is not stopped
                     there are _ small cases and the way to solve:
                                        [["o", " ", " "],
                                         [" ", "x", " "],
                                         ["o", " ", "x"]]
                        or
                                        [["x", " ", " "],           [["x", " ", " "],
                                         [" ", "o", " "],  or        [" ", "o", " "],
                                         [" ", "x", "o"]]            [" ", "o", "x"]]

                    """
                    move = move_to_win_and_defense(board, human_comp[0])
                    if move:
                        board[move[0]][move[1]] = human_comp[1]
                    else:
                        if not check_letter(board, [1, 1], human_comp[0]):
                            if check_letter(board, [0, 0], human_comp[0]):
                                if (check_letter(board, [2, 1], human_comp[0]) or
                                        check_letter(board, [1, 2], human_comp[0])):
                                    board[2][2] = human_comp[1]
                                else:
                                    board[2][1] = human_comp[1]
                            elif check_letter(board, [0, 2], human_comp[0]):
                                if (check_letter(board, [1, 0], human_comp[0]) or
                                        check_letter(board, [2, 1], human_comp[0])):
                                    board[2][0] = human_comp[1]
                                else:
                                    board[1][0] = human_comp[1]
                            elif check_letter(board, [2, 0], human_comp[0]):
                                if (check_letter(board, [0, 1], human_comp[0]) or
                                        check_letter(board, [1, 2], human_comp[0])):
                                    board[0][2] = human_comp[1]
                                else:
                                    board[1][2] = human_comp[1]
                            elif check_letter(board, [2, 2], human_comp[0]):
                                if (check_letter(board, [0, 1], human_comp[0]) or
                                        check_letter(board, [1, 0], human_comp[0])):
                                    board[0][0] = human_comp[1]
                                else:
                                    board[0][1] = human_comp[1]
                            else:
                                if check_letter(board, [0, 1], human_comp[0]):
                                    board[0][2] = human_comp[1]
                                elif check_letter(board, [1, 0], human_comp[0]):
                                    board[0][0] = human_comp[1]
                                elif check_letter(board, [1, 2], human_comp[0]):
                                    board[2][2] = human_comp[1]
                                else:
                                    board[2][0] = human_comp[1]
                        else:
                            if check_letter(board, [2, 2], human_comp[0]):
                                board[2][0] = human_comp[1]
                case 6:
                    """
                    There are three steps in this stage:
                    1st: Check whether there are any ways for computer to win the game
                    2nd: Check whether there are any ways for computer to lose the game
                    3rd: Block suitable block resulting a draw
                    """
                    move = move_to_win_and_defense(board, human_comp[1])
                    if move:
                        board[move[0]][move[1]] = human_comp[1]
                    else:
                        move = move_to_win_and_defense(board, human_comp[0])
                        if move:
                            board[move[0]][move[1]] = human_comp[1]
                        else:
                            if check_letter(board, [0, 0]):
                                board[0][0] = human_comp[1]
                            elif check_letter(board, [2, 0]):
                                board[2][0] = human_comp[1]
                            elif check_letter(board, [0, 2]):
                                board[0][2] = human_comp[1]
                            elif check_letter(board, [2, 2]):
                                board[2][2] = human_comp[1]
                            else:
                                check = 0
                                for row in range(3):
                                    for col in range(3):
                                        if check_letter(board, [row, col]):
                                            board[row][col] = human_comp[1]
                                            check = 1
                                            break
                                    if check == 1:
                                        break
                case 8:
                    """
                    The same as the recent stage
                    """
                    move = move_to_win_and_defense(board, human_comp[1])
                    if move:
                        board[move[0]][move[1]] = human_comp[1]
                    else:
                        move = move_to_win_and_defense(board, human_comp[0])
                        if move:
                            board[move[0]][move[1]] = human_comp[1]
                        else:
                            check = 0
                            for row in range(3):
                                for col in range(3):
                                    if check_letter(board, [row, col]):
                                        board[row][col] = human_comp[1]
                                        check = 1
                                        break
                                if check == 1:
                                    break
                case _:
                    """
                        human turn
                    """
                    while True:
                        try:
                            decision = [int(x) for x in
                                        input("Enter your move with coordinate x, y in range [0-2]: ")
                                        .strip().split(", ")]
                        except ValueError:
                            print("Input should be format as x, y separated by a comma and a space and in range [0-2]")
                        else:
                            if decision[0] in range(3) and decision[1] in range(3) and check_letter(board, decision):
                                break
                            else:
                                print("Input should be different and in range [0-2]")
                    board[decision[0]][decision[1]] = human_comp[0]
            order += 1
        else:
            """
                computer goes first: lead to draw or win for computer
            """
            match order:
                case 1:
                    """
                    start with a very strong move at the corner:
                                [["x", " ", " "],
                                 [" ", " ", " "],
                                 [" ", " ", " "]]
                    """
                    board[0][0] = human_comp[1]
                case 3:
                    """
                        [["o", "#x", " "],
                         [" ", "#x", "#x"],
                         ["#x", " ", " "]]
                    """
                    if ((check_letter(board, [0, 1], human_comp[0]) or check_letter(board, [1, 2], human_comp[0])
                            or check_letter(board, [0, 2], human_comp[0]))
                            or check_letter(board, [1, 1], human_comp[0])):
                        board[2][0] = human_comp[1]
                    else:
                        board[0][2] = human_comp[1]
                case 5:
                    """
                        there are 2 steps:
                        1st: check if there is a way to win
                        2nd: there are two big cases:
                            first:
                                [["x", " ", " "],
                                 [" ", " ", " "],
                                 ["x", " ", " "]]

                                 case 1:
                                         [["x", " ", " "],
                                          ["o", "o", "x"],
                                          ["x", " ", " "]]
                                 case 2:
                                        [["x", " ", " "],
                                         ["o", "x", "o"],
                                         ["x", " ", " "]]
                                 case 3:
                                        [["x", "o", "x"],
                                         [" ", " ", " "],
                                         ["x", " ", "o"]]
                                 case 4:
                                         [["x", " ", "o"],
                                          ["o", " ", " "],
                                          ["x", " ", "x"]]

                            second:
                                [["x", " ", "x"],
                                 [" ", " ", " "],
                                 [" ", " ", " "]]
                                case 1:
                                        [["x", "o", "x"],
                                         [" ", "x", " "],
                                         [" ", "o", " "]]
                                case 2:
                                        [["x", "o", "x"],
                                         ["o", " ", " "],
                                         [" ", " ", "x"]]
                                case 3:
                                        [["x", "o", "x"],
                                         [" ", " ", " "],
                                         ["o", " ", "x"]]

                    """
                    move = move_to_win_and_defense(board, human_comp[1])
                    if move:
                        board[move[0]][move[1]] = human_comp[1]
                    else:
                        if check_letter(board, [2, 0], human_comp[1]):
                            if check_letter(board, [1, 1], human_comp[0]):
                                board[1][2] = human_comp[1]
                            elif check_letter(board, [1, 2], human_comp[0]):
                                board[1][1] = human_comp[1]
                            elif check_letter(board, [2, 2], human_comp[0]):
                                board[0][2] = human_comp[1]
                            else:
                                board[2][2] = human_comp[1]
                        else:
                            if check_letter(board, [2, 1], human_comp[0]):
                                board[1][1] = human_comp[1]
                            else:
                                board[2][2] = human_comp[1]
                case 7:
                    """
                        There are _ steps in this stage:
                        1st: Check whether there are any ways for computer to win the game
                        2nd: Check whether there are any ways for computer to lose the game
                        3rd: Play a possible case that lead to draw

                    """
                    if check_letter(board, [1, 1], human_comp[1]):
                        move = move_to_win_and_defense(board, human_comp[1])
                        if move:
                            board[move[0]][move[1]] = human_comp[1]
                    else:
                        move = move_to_win_and_defense(board, human_comp[0])
                        if move:
                            board[move[0]][move[1]] = human_comp[1]
                        else:
                            check = 0
                            for row in range(3):
                                for col in range(3):
                                    if check_letter(board, [row, col]):
                                        board[row][col] = human_comp[1]
                                        check = 1
                                        break
                                if check == 1:
                                    break
                case 9:
                    """
                        find the last box and write on it
                    """
                    for row in range(3):
                        for col in range(3):
                            if check_letter(board, [row, col]):
                                board[row][col] = human_comp[1]
                case _:
                    """
                        human turn
                    """
                    while True:
                        try:
                            decision = [int(x) for x in
                                        input("Enter your move with coordinate x, y in range [0-2]: ")
                                        .strip().split(", ")]
                        except ValueError:
                            print("Input should be format as x, y separated by a comma and a space and in range [0-2]")
                        else:
                            if decision[0] in range(3) and decision[1] in range(3) and check_letter(board, decision):
                                break
                            else:
                                print("Input should be different and in range [0-2]")
                    board[decision[0]][decision[1]] = human_comp[0]
            order += 1
        print(draw_board(board))
        if game_over(board, human_comp[0]) or game_over(board, human_comp[1]) or is_full(board):
            break
    if game_over(board, human_comp[0]):
        print("You won")
    elif game_over(board, human_comp[1]):
        print("You lost")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
