# Passed batch 1, TLE for batch 2
import sys
input = sys.stdin.readline

def check_rows():
    c = 0
    for x in range(n):
        valid = []
        stars = []
        for y in range(m):
            if board[x][y] == ".":
                valid.append(y)
                stars.append(0)
            elif board[x][y] == "*":
                for i in range(len(stars)):
                    stars[i] += 1
        for i in range(len(stars)):
            if stars[i] >= 2:
                board[x] = board[x][:valid[i]]+"c"+board[x][valid[i]+1:]
                c += 1

    for x in range(n):
        valid = []
        stars = []
        for y in reversed(range(m)):
            if board[x][y] == ".":
                valid.append(y)
                stars.append(0)
            elif board[x][y] == "*":
                for i in range(len(stars)):
                    stars[i] += 1
        for i in range(len(stars)):
            if stars[i] >= 2:
                board[x] = board[x][:valid[i]]+"c"+board[x][valid[i]+1:]
                c += 1
                
    return c

def check_cols():
    c = 0
    for x in range(m):
        valid = []
        stars = []
        for y in range(n):
            if board[y][x] == ".":
                valid.append(y)
                stars.append(0)
            elif board[y][x] == "*":
                for i in range(len(stars)):
                    stars[i] += 1
        for i in range(len(stars)):
            if stars[i] >= 2:
                board[valid[i]] = board[valid[i]][:x]+"c"+board[valid[i]][x+1:]
                c += 1

    for x in range(m):
        valid = []
        stars = []
        for y in reversed(range(n)):
            if board[y][x] == ".":
                valid.append(y)
                stars.append(0)
            elif board[y][x] == "*":
                for i in range(len(stars)):
                    stars[i] += 1
        for i in range(len(stars)):
            if stars[i] >= 2:
                board[valid[i]] = board[valid[i]][:x]+"c"+board[valid[i]][x+1:]
                c += 1
                
    return c
                
n, m = [int(x) for x in input().split(" ")]
board = [[] for _ in range(n)]

for x in range(n):
    board[x] = input()

c = 0
c += check_rows()
c += check_cols()
print(c)
