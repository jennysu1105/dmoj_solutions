def swap(b1, b2):
    temp = b[b1]
    b[b1] = b[b2]
    b[b2] = temp
s = int(raw_input())
n = int(raw_input())
b = []
for x in xrange(n):
    l = map(int, raw_input().split())
    l.append(x + 1)
    b.append(l)
q = int(raw_input())
o = [int(raw_input()) for _ in xrange(q)]

b.sort()
b.reverse()

for x in xrange(n-1):
    if b[x][0] == b[x+1][0] and b[x][0] >= s and b[x][2] < b[x+1][2]:
        swap(x, x+1)
    elif b[x][0] == b[x+1][0] and b[x][0] < s and b[x][1] < b[x+1][1]:
        swap(x, x+1)
for x in o:
    print b[x-1][3]
