n = int(raw_input())
b = raw_input()
a = raw_input()

same = 0
for i in xrange(n):
    if a[i] == 'C' and a[i] == b[i]:
        same += 1
print same
