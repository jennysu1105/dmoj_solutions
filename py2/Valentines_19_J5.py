def meet(p1, p2):
    if (p1[0] == p2[0]) and (p1[1] != p2[1]):
        return False
    return True

n = int(raw_input())
arr = []
for x in xrange(n):
    arr.append(map(int, raw_input().split()))

if n == 1:
    print 0

else:
    pairs = 0
    for t in xrange(n):
        for x in xrange(t+1, n):
            if meet(arr[t], arr[x]):
                pairs += 1
        
    print pairs
