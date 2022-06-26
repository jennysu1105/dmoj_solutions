#7/10

import sys
input = sys.stdin.readline

n1, n2, n3 = [int(x) for x in input().split(" ")]
b = 0
p = 0

for i in reversed(range(n3)):
    if (n1 >= 2**i and n2 >= 2**i) and (n1%2 == 1 and n2%2 == 1):
        p += 1
    elif (n1 >= 2**i and n1%2 == 1) or (n2 >= 2**i and n2%2 == 1):
        b += 1
    else:
        p += 1

    if n1 >= 2**i:
        n1 = n1 // 2
    if n2 >= 2**i:
        n2 = n2 // 2
        

print(b, p)
