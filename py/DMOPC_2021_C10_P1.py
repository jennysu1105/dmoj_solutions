# TDE: test 3+
def test(s):
    i=0
    while i < len(s):
        if s[i] in letters:
            if i == len(s)-1:
                return "NO"
            if s[i] == "h" and s[i+1]=="u":
                return "NO"
            if s[i] == "f" and s[i+1]!="u":
                return "NO"
            if s[i+1] not in vowels:
                return "NO"
            i += 2
        else:
            if s[i] not in vowels:
                return "NO"
            i += 1
    return "YES"
            
n = int(input())
vowels = ["a", "i", "u", "e", "o"]
letters = ["k", "n", "h", "m", "r", "f"]

for x in range(n):
    print(test(input()))
