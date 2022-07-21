num = []
for x in xrange(4):
    num.append(int(raw_input()))

if num[0] not in [8, 9] or num[3] not in [8,9]:
    print "answer"
elif num[1] != num[2]:
    print "answer"
else:
    print "ignore"
