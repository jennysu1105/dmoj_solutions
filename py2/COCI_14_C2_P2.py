n = int(raw_input())
arr = []
for x in xrange(n):
    arr.append(raw_input())
for x in xrange(n-1):
    arr.remove(raw_input())
print arr[0]
