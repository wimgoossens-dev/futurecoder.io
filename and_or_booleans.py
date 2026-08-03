# This test-function is needed for making the code work
def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {actual!r} != {expected!r}")

def diagonal_winner(board):
    middle = board[1][1]
    return (
            (middle == board[0][0] and middle == board[2][2]) or
            (middle == board[0][2] and middle == board[2][0])
    )

assert_equal(
    diagonal_winner(
        [
            ['X', 'O', 'X'],
            ['X', 'X', 'O'],
            ['O', 'O', 'X']
        ]
    ),
    True
)

assert_equal(
    diagonal_winner(
        [
            ['X', 'X', 'O'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X']
        ]
    ),
    True
)

assert_equal(
    diagonal_winner(
        [
            ['O', 'X', 'O'],
            ['X', 'X', 'X'],
            ['O', 'O', 'X']
        ]
    ),
    False
)