# TLE: Test 3+
import sys
input = sys.stdin.readline

n = int(input())

total = n*2 - 1
for x in range(1,n+1):
    for y in range(2,x):
        if x % y == 0:
            total += 1

print(total)
