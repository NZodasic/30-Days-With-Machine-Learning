# sudoku_input.py

def input_sudoku():
    board = []
    print("Input sudoku table 9x9:")
    for i in range(9):
        row = list(map(int, input(f"Line {i+1}: ").split()))
        if len(row) != 9:
            raise ValueError("Each line must contain exactly 9 numbers!")
        board.append(row)
    return board


def is_valid_sudoku(board):
    def check_group(numbers):
        nums = [n for n in numbers if n != 0]
        return len(nums) == len(set(nums))

    for row in board:
        if not check_group(row):
            return False

    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not check_group(column):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = []
            for r in range(3):
                for c in range(3):
                    block.append(board[i+r][j+c])
            if not check_group(block):
                return False

    return True

if __name__ == "__main__":
    sudoku_board = input_sudoku()
    print("Sudoku Validator:", is_valid_sudoku(sudoku_board))