#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 12:24:50 2018

@author: sorin
"""

n = int(input())
a = [int(i) for i in input().split(' ')]

minswap = 0
for i, j in enumerate(a):
    #print(i)
    for k in a[i:]:
        if j > k:
            minswap += 1

print(minswap)
