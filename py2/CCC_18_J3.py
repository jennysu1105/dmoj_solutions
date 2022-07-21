def getLoc():
    arr = [0]
    for x in d:
        arr.append(arr[len(arr)-1] + x)
    return arr

d = map(int, raw_input().split())

loc = getLoc()
for n in xrange(5):
    for m in xrange(5):
        print abs(loc[n]-loc[m]),
    print
