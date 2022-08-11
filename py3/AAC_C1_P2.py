import sys
import math
input = sys.stdin.readline

info = [int(x) for x in input().split(" ")]
opp = []

for i in range(info[0]):
    opp.append(int(input()))

alpaca = int(input())
for i in range(info[0]):
    while opp[i] >= alpaca:
        opp[i] = math.floor(opp[i]*(100-info[3])/100)
        info[2] -= 1
        if info[2] < 0:
            print("NO")
            break
    if info[2] < 0:
        break

if info[2] >= 0:
        print("YES")
