c1 = input()
c2 = input()

if c2[len(c2)-1] == "s":
    print(c1+"-tu les "+c2+" ?")
elif c2[len(c2)-1] == "e":
    print(c1+"-tu la "+c2+" ?")
else:
    print(c1+"-tu le "+c2+" ?")
