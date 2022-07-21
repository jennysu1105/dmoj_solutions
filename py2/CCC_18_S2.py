def rotateArr():
    newArr = []
    for col in xrange(n):
        line = []
        for x in xrange(n):
            line.append(arr[n-1-x][col])
        newArr.append(line)
    return newArr
            
def correctRow():
    if arr[0][0] > arr[0][1]:
        return False
    return True

def correctCol():
    if arr[0][0] > arr[1][0]:
        return False
    return True

n = int(raw_input())

arr = []
for x in xrange(n):
    arr.append(map(int, raw_input().split()))

while(True):
    if correctRow() and correctCol():
        break
    else:
        arr = rotateArr()

for x in xrange(n):
    print " ".join(map(str, arr[x]))
