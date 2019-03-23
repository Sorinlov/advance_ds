#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:36:16 2018

@author: sorin
"""

n = int(input().strip())
a = list(map(int, input().split(' ')))

for i in range(1, n+1):
    b = a[:2*i-1]
    b.sort()
    print(b[i-1])
    