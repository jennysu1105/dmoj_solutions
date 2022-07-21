for t in xrange(10):
    n = int(raw_input())
    arr = []
    for x in xrange(n):
        arr.append(map(int, raw_input().split()))
    roads = [arr[0][0]]
    srb = min(arr[0][2:])
    for r in xrange(1,n):
        sr = min(arr[r][2:])
        if srb > sr:
            srb = sr
            roads = [arr[r][0]]
        elif srb == sr:
            roads.append(arr[r][0])
    roads.sort()
    roads = map(str, roads)
    print srb, "{" + ",".join(roads) + "}"
