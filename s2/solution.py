
#!/usr/bin/env python3

import re

with open('input.txt', 'r') as f: 
    data = f.readlines()

r1 = 0
x = [list(map(int, re.findall(r'\d+', i))) for i in data]
for report in x:
    ref = list(map(lambda x: report[x+1]-report[x],range(len(report)-1)))

    n = all([i<0 for i in ref]) and all([abs(i) in range(1,4) for i in ref])
    p = all([i>0 for i in ref]) and all([i in range(1,4) for i in ref])
    if n or p:
        r1 += 1

r2 = 0
for report in x:
    for k in range(len(report)):
        temp = report[:k] + report[k+1:]
        ref = list(map(lambda x: temp[x+1]-temp[x],range(len(temp)-1)))

        n = all([i<0 for i in ref]) and all([abs(i) in range(1,4) for i in ref])
        p = all([i>0 for i in ref]) and all([i in range(1,4) for i in ref])
        if n or p:
            r2 += 1
            break
print(r1, r2)



