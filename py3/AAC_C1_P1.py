import sys
input = sys.stdin.readline

sr = [int(x) for x in input().split(" ")]

if sr[0]**2 > 3.14*sr[1]**2:
    print("SQUARE")

else:
    print("CIRCLE")
