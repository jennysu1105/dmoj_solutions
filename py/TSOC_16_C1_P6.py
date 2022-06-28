# Pass 1st Test Case
import sys
input = sys.stdin.readline
def lcs(lx, ly, x, y):
    lcsTable = [[0 for k in range(ly+1)] for l in range(lx+1)]

    result = 0
    for i in range(lx+1):
        for j in range(ly+1):
            if i==0 or j==0:
                lcsTable[i][j] = 0
            elif x[i-1] == y[j-1]:
                lcsTable[i][j] = lcsTable[i-1][j-1]+1
                result = max(result, lcsTable[i][j])
            else:
                lcsTable[i][j] = 0
                
    return result

n, m = [int(x) for x in input().split(" ")]
s1 = input()
s2 = input()

lcstring = lcs(n, m, s1, s2)
if lcstring%2 == 1:
    lcstring -= 1

print(n,m,lcstring)
print(max((n-lcstring)//2, (m-lcstring)//2))
