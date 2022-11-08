# WA: Test Case #7
import sys
import math
input = sys.stdin.readline

a, b = [int(x) for x in input().split(" ")]

def findFactor(n):
    def get_factor(n):
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1

        while factor == 1:
            for count in range(cycle_size):
                if factor > 1: break
                x = (x*x+1)%n
                factor = math.gcd(x-x_fixed,n)

            cycle_size *=2
            x_fixed = x

        return factor
    while n>1:
        next = get_factor(n)
        if (next + b//next == a):
            return min(next, b//next), max(next, b//next)
        n //= next
    for x in range(next + 1, b):
        if (x + b//x == a):
            return min(x, b//x), max(x, b//x)

b_dup = b
c, d = findFactor(b_dup)

print(str(c) + " " + str(d))
