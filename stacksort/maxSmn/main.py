#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:35:47 2018

@author: sorin
"""

def maxshist(hight):
    h = []
    h[:] = hight[:]
    h.insert(0, -1)
    h.append(-1)

    stack = []
    maxs = 0
    i = 0
    while i < len(h):
        if len(stack) == 0 or h[stack[-1]] <= h[i]:
            stack.append(i)
            i += 1
        else:
            k = stack.pop()
            hight = h[k]
            wide = i - stack[-1] -1
            maxs = max(maxs, hight*wide)
    return maxs


    

if __name__ == '__main__':
    n,m = map(int, input().split())
    mat = []
    for i in range(n):
        mat.append(input().strip())
    
    h = [0 for i in range(m)]
    maxs = 0
    for row in range(n):
        for i, s in enumerate(mat[row]):
            if s == '.':
                h[i] = h[i] + 1
            else:
                h[i] = 0
        maxs = max(maxs, maxshist(h))
    print(maxs)