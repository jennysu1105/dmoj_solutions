t = int(raw_input())
n = int(raw_input())
d = map(int, raw_input().split())
d.sort()
p = map(int, raw_input().split())
p.sort()

speed = 0
if t == 2:
    p.reverse()
for x in xrange(n):
    speed += max(d[x], p[x])
print speed
