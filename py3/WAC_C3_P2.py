'''  Wesley's Anger Contest 3 Problem 2
     100/100 - 5 pts
'''
import sys
input = sys.stdin.readline

n = int(input())

for x in range(n):
    d = int(input())
    if d%3 == 0:
        print((d//3)**3)
    elif d%3 == 1:
        print(((d//3)**2)*(d//3+1))
    else:
        print(((d//3+1)**2)*(d//3))
