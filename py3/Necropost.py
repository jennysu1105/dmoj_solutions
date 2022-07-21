import sys
from datetime import datetime

input = sys.stdin.readline

s1 = input()
s2 = input()
start = datetime.strptime(s1[:len(s1)-1], "%Y/%m/%d")
finish = datetime.strptime(s2[:len(s2)-1], "%Y/%m/%d")

difference = finish-start
print(difference.days)
