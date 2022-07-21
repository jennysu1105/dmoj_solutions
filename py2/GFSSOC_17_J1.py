c, n = map(int, raw_input().split())
b = 0
cD = 0
for x in [raw_input() for _ in xrange(c)]:
    if x == "TOK":
        b += 1
    elif x == "English":
        b += 2
    elif x == "Chemistry":
        b += 3
    elif x == "Math":
        b += 4
    if b > n:
        print "Go to Metro"
        print cD
        break
    cD += 1
if b <= n:
    print "YEA BOI"
