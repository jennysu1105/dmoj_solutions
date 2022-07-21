def split(sl, al):
    return s[sl:], a[al:]  

s = list(raw_input())
s.sort()
a = list(raw_input())
a.sort()

if s == a:
    print "A"
else:
    ast = a.count('*')
    a = a[ast:]
    while(True):
        if (len(s) != 0):
            letter = s[0]
            sl = s.count(letter)
            al = a.count(letter)
            if sl < al:
                print "N"
                break
            elif sl == al:
                s, a = split(sl, al)
            else:
                ast -= sl - al
                if ast < 0:
                    print "N"
                    break
                s, a = split(sl, al)
        else:
            print "A"
            break
