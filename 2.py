import re, sys

with open('2.txt') as f:
    pwds = f.readlines()

formula = re.compile(r'(\d{1,2})-(\d{1,2})\s([a-z]):\s([a-z]+)')
count = 0
for line in pwds:
    res = formula.match(line)
    if int(res[1]) <= res[4].count(res[3]) <= int(res[2]):
        count += 1 
print(count)
