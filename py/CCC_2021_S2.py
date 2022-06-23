m = int(input())
n = int(input())
k = int(input())

arr = []
for x in range(m):
    arr.append([])
    for y in range(n):
        arr[x].append(False)

count = 0

for y in range(k):
    t, x = input().split(" ")
    x = int(x)
    if t == "C":
        for c in range(m):
            arr[c][x-1] = not arr[c][x-1]
            if arr[c][x-1]:
                count += 1
            else:
                count -= 1
    else:
        for c in range(n):
            arr[x-1][c] = not arr[x-1][c]
            if arr[x-1][c]:
                count += 1
            else:
                count -= 1

print(count)
