def best_case():
    i = 1
    rem = 0
    for i in range(n-1):
        pickup[i-1] -= dropoff[i]
        if pickup[i-1] > 0 and i != 1:
            rem += pickup[i-1]
        elif pickup[i-1] < 0 and i != 1:
            rem -= pickup[i-1]
    if rem < 0:
        pickup[0] += rem 
    if pickup[0] < 0 :
        pickup[0] = 0
    return pickup[0]

def worst_case():
    init = pickup[0]
    for x in dropoff:
        init -= x
        if init <= 0:
            return 0
    return init

n = int(input())

pickup = []
dropoff = []
for x in range(n-1):
    l = input().split(" ")
    pickup.append(int(l[0]))
    dropoff.append(int(l[1]))

print(worst_case())
print(best_case())
