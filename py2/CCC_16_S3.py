from collections import deque
class Node():
    def __init__(self, num, s):
        self.s = s
        self.edges = []
        self.num = num
    def addEdge(self, num):
        self.edges.append(num)

def getStart(s):
    for x in arr:
        if s in x:
            return Node(s, 0)
        
def getEdge(no):
    for x in arr:
        if no.num in x:
            if x.index(no.num) == 0:
                no.addEdge(x[1])
            else:
                no.addEdge(x[0])

def search():
    visited = []
    q = deque([getStart(cur)])
    while(True):
        getEdge(q[0])
        for e in q[0].edges:
            if e in p:
                p.remove(e)
                return e, q[0].s + 1
            elif e not in visited:
                q.append(Node(e, q[0].s + 1))
                visited.append(e)
        q.popleft()
        
n, m = map(int, raw_input().split())
p = map(int, raw_input().split())
arr = []
for x in xrange(n-1):
    arr.append(map(int, raw_input().split()))

org = p[:]
allS = []
for x in org:
    p = org[:]
    cur = x
    p.remove(cur)
    steps = 0
    while(len(p) != 0):
        cur, step = search()
        steps += step
    allS.append(steps)
allS.sort()
print allS[0]
