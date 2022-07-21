n = int(raw_input())
arr = []
for x in xrange(n):
    arr.append(map(int, raw_input().split()))

pink = 0
for c in arr:
    if (c[0] < 240) or (c[0] > 255):
        continue
    if (c[1] < 0) or (c[1] > 200):
        continue
    if (c[2] < 95) or (c[2] > 220):
        continue
    pink += 1

print pink
