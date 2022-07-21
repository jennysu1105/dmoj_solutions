import sys

nBlock = int(input())

h = list(map(int, input().split(" ")))
l = list(map(int, input().split(" ")))

prev = (0, h[0])
det = 0
len = 0
for i in range(nBlock):
    len += l[i]
    det += prev[0]*h[i+1] - len*prev[1]
    prev = (len, h[i+1])

det += -prev[0]*prev[1]

print(abs(det)/2)
