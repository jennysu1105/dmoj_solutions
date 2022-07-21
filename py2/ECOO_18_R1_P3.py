def modify(l):
    m = []
    for key in l:
        if key == 0:
            m.append(str(z))        
        elif key%2 == 0:
            m.append(str(key + x))
        else:
            if key - y < 0:
                m.append(str(0))
                continue
            m.append(str(key - y))
    return m
for i in xrange(10):
    n, x, y, z = map(int, raw_input().split())
    k = []
    for n in xrange(n):
        k.append(modify(map(int, list(raw_input()))))
    raw_input()
    failed = []
    for n in xrange(n + 1):
        if "".join(k[n]) != raw_input():
            failed.append(str(n + 1))
    
    if len(failed) == 0:
        print "MATCH"
    else:
        print "FAIL: " + ",".join(failed)
    raw_input()
