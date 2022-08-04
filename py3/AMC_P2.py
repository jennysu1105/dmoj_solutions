import sys
input = sys.stdin.readline

n = int(input())

arr = [int(x) for x in input().split(" ")]

ans = 0

for i in range(n):
    ans += arr[i]

print((ans * 2**(n-1))%1000000007)
