def findLeft(index):
    return abs((arr[index]-arr[index-1])/2.0)

def findRight(index):
    return abs((arr[index+1] - arr[index])/2.0)

n = int(raw_input())

arr = []
for x in range(n):
    arr.append(int(raw_input()))

arr.sort()

smallest = findLeft(1) + findRight(1)

for x in xrange(len(arr) - 3):
    if ((findLeft(x + 2) + findRight(x + 2))<smallest):
        smallest = findLeft(x + 2) + findRight(x + 2)
    
print smallest
