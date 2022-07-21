import sys
input = sys.stdin.readline

row, col = [int(x) for x in input().split(" ")]
board = [[] for _ in range(row)]
rectangles = 0

for r in range(row):
    board[r] = [char for char in input()]
    for c in range(col):
        if board[r][c] == "*":
            if r > 0:
                if board[r-1][c] == "*":
                    continue
            if c > 0:
                if board[r][c-1] == "*":
                    continue
            rectangles += 1

print(rectangles)
