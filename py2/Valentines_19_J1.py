n = int(raw_input())
scores = []
for x in xrange(n):
    scores.append(int(raw_input()))
ranking = []
for p in scores:
    if (p < 1000):
        ranking.append("Newbie")
    elif (p >= 1000) and (p < 1200):
        ranking.append("Amateur")
    elif (p >= 1200) and (p < 1500):
        ranking.append("Expert")
    elif (p >= 1500) and (p < 1800):
        ranking.append("Candidate Master")
    elif (p >= 1800) and (p < 2200):
        ranking.append("Master")
    elif (p >= 2200) and (p < 3000):
        ranking.append("Grandmaster")
    elif (p >= 3000) and (p < 4000):
        ranking.append("Target")    
    else:
        ranking.append("Rainbow Master")

for r in ranking:
    print r
