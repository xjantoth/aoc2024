#!/usr/bin/env python3

import re

with open('input.txt', 'r') as f: 
    data = f.readlines()

l, r = [], []
[{l.append(x[0]), r.append(x[1])} for x in [re.findall(r'\d+', i) for i in data]]

r1 = sum([abs(int(a) - int(b)) for a, b in zip(sorted(l), sorted(r))])
r2 = sum([int(i)*[int(x) for x in r].count(i) for i in [int(ll) for ll in l]])
print(r1, r2)
