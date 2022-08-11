# TLE Batch 3 #2
import sys
input = sys.stdin.readline

def check_perms(l, x):
    l = list(set(l))
    while len(l) > 1:
        for n in l[1:]:
            if l[0]*n == x and n != l[0]:
                return "YES"
        l = l[1:]
    return "NO"
        
nq = [int(x) for x in input().split(" ")]

a = [int(x) for x in input().split(" ")]

for _ in range(nq[1]):
    q = [int(x) for x in input().split(" ")]

    print(check_perms(a[q[0]-1:q[1]],q[2]))
