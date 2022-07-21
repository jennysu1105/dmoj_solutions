for times in xrange(10):
    t, n = map(int, raw_input().split())
    arr = []
    for x in xrange(n):
        arr.append(raw_input())
    
    wTimer = 0
    bWaiting = 0
    total = n
    
    for x in xrange(0, n):
        if arr[x] == "B":
            bWaiting += 1
        if wTimer == 0 and bWaiting != 0:
            bWaiting -= 1
            wTimer = t
        if wTimer == 0 and bWaiting == 0:
            continue
        wTimer -= 1
        
    total += wTimer + bWaiting*t
    print total-n
