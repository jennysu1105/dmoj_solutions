#Batch 1 pass
def query2(l, r):
    sum = 0
    while l <= r:
        sum += arr[l-1]
        l += 2
    print(sum)

def query1(i, j):
    arr[i-1] = j
    
n, q = [int(x) for x in input().split(" ")]
arr = [int(x) for x in input().split(" ")]

for x in range(n):
    qr = [int(x) for x in input().split(" ")]
    if qr[0] == 1:
        query1(qr[1], qr[2])
    else:
        query2(qr[1], qr[2])
