#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Nov 26 18:13:00 2018

@author: sorin
"""

def getAnswer(r):
    r.insert(0, float('inf'))
    s = []
    t = r.pop()
    while len(r) > 0:
        if len(s) == 0 or s[-1] <= t:
            s.append(t)
            t = r.pop()
        else:
            r.append(s.pop())
    for result in s:
        print(result)


n = map(int, input().strip())
r = list(map(int, input().split()))
getAnswer(r)
