# TLE
import sys
input = sys.stdin.readline

def query(l, r):
    best = max(sum(line1[l-1:l]), sum(line2[l:r-1]))
    k=l+1
    while k <= r:
        cur = max(sum(line1[l-1:k]), sum(line2[k:r-1]))
        if best != min(best, cur):
            best = cur
        k+=1
    print(best)
    
n, q = [int(x) for x in input().split(" ")[:2]]

line1 = [int(x) for x in input().split(" ")[:n]]
line2 = [int(x) for x in input().split(" ")[:n]]

for _ in range(q):
    x, y = [int(x) for x in input().split(" ")]
    query(x, y)
