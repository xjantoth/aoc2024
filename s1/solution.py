#!/usr/bin/env python3

import re

with open('input.txt', 'r') as f: 
    data = f.readlines()

l, r = [], []
[{l.append(x[0]), r.append(x[1])} for x in [list(map(int, re.findall(r'\d+', i))) for i in data]]

r1 = sum([abs(a - b) for a, b in zip(sorted(l), sorted(r))])
r2 = sum([i*r.count(i) for i in l])
print(r1, r2)
