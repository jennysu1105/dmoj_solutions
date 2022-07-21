# Passed batch 1, TLE for batch 2
import sys
input = sys.stdin.readline

def query(seq):
    stack = []
    for c in seq:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if len(stack) == 0:
                stack.append(c)
            elif stack[len(stack)-1] == "(":
                stack.pop()
            else:
                stack.append(c)
    if ")" in stack and "(" in stack:
        print ("NO")
        return
    print ("YES")
    
n, q = [int(x) for x in input().split(" ")[0:2]]

line = input()

for _ in range(q):
    l, r = [int(x) for x in input().split(" ")]
    query(line[l-1:r])
