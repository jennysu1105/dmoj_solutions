n = int(raw_input())
arr = map(int, raw_input().split())

if n%2 == 0:
    arr.sort()
    l = arr[:n/2]
    l.reverse()
    h = arr[n/2:]
    for x in xrange(n/2):
        print l[x], h[x],    
else:
    arr.sort()
    l = arr[:n/2+1]
    l.reverse()
    h = arr[n/2+1:] 
    for x in xrange(n/2):
        print l[x], h[x],
    print l[n/2]
