def isinRange(sudoku):
    N = 9
    for i in range(0, N):
        for j in range(0, N):
            if ((sudoku[i][j] <= 0) or
                    (sudoku[i][j] > 9)):
                return False
    return True


def isValid(sudoku):
    N = 9
    if (isinRange(sudoku) == False):
        return False

    unique = [False] * (N + 1)

    for i in range(0, N):
        for m in range(0, N + 1):
            unique[m] = False

        for j in range(0, N):
            Z = sudoku[i][j]

            if (unique[Z] == True):
                return False
            unique[Z] = True

    for i in range(0, N):
        for m in range(0, N + 1):
            unique[m] = False

        for j in range(0, N):
            Z = sudoku[j][i]

            if (unique[Z] == True):
                return False
            unique[Z] = True

    for i in range(0, N - 2, 3):
        for j in range(0, N - 2, 3):

            for m in range(0, N + 1):
                unique[m] = False

            for k in range(0, 3):
                for l in range(0, 3):
                    # Stores row number
                    # of current block
                    X = i + k
                    # Stores column number
                    # of current block
                    Y = j + l
                    # Stores the value
                    # of board[X][Y]
                    Z = sudoku[X][Y]
                    # Check if current block
                    # stores duplicate value
                    if (unique[Z] == True):
                        return False
                    unique[Z] = True
    return True


if __name__ == '__main__':

    sudoku = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
              [4, 5, 6, 7, 8, 9, 1, 2, 3],
              [7, 8, 9, 1, 2, 3, 4, 5, 6],
              [9, 1, 2, 3, 4, 5, 6, 7, 8],
              [3, 4, 5, 6, 7, 8, 9, 1, 2],
              [6, 7, 8, 9, 1, 2, 3, 4, 5],
              [8, 9, 1, 2, 3, 4, 5, 6, 7],
              [2, 3, 4, 5, 6, 7, 8, 9, 1],
              [5, 6, 7, 8, 9, 1, 2, 3, 4]]

    if (isValid(sudoku)):
        print("True")
    else:
        print("False")
