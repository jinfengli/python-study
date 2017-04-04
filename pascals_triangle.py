#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def pascals_triangle():
    q = [1]
    while True:
        yield q
        for i in range(1, len(q)):
            q[i] = p[i-1] + p[i]
        q.append(1)
        p = q[:]

		
n = 0
for t in pascals_triangle():
    print(t)
	print('----')
    n = n + 1
    if n == 10:
        break