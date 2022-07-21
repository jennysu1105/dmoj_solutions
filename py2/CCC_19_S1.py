def flipV():
  l[0].reverse()
  l[1].reverse()

def flipH():
  for x in [0, 1]:
    temp = l[0][x]
    l[0][x] = l[1][x]
    l[1][x] = temp

arr = list(raw_input())
l = [[1, 2], [3, 4]]

h = arr.count('H')
v = arr.count('V')
if v%2 == 1:
  flipV()
if h%2 == 1:
  flipH()

for x in [0,1]:
  print l[x][0], l[x][1]
