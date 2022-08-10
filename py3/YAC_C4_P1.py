import sys
input = sys.stdin.readline

def analyze():
    matches = 0
    for i in range(n):
        if deck[i] == deck[i+n]:
            matches += 1

    return matches
    
n = int(input())

deck = [int(x) for x in input().split(" ")]

print(analyze())
