def different(seqA, seqB):
    mid = len(seqA)//2
    A = seqA[:mid] != seqB[:mid]
    B = seqA[mid:] != seqB[mid:]
    if len(seqA) == 1:
        return "LARRY IS SAVED!"
    elif (A and B) or (not A and not B):
        return "LARRY IS DEAD!"
    elif A:
        return different(seqA[:mid], seqB[:mid])
    else:
        return different(seqA[mid:], seqB[mid:])
    
A = input()
B = input()
if len(A) == 1:
    print("LARRY IS SAVED!")
else:
    print(different(A, B))
