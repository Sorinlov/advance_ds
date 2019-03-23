#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 00:32:24 2018

@author: sorin
"""


'''
n = int(input())
a = [int(i) for i in input().split(' ')]

minswap = 0
for i, j in enumerate(a):
    #print(i)
    for k in a[i:]:
        if j > k:
            minswap += 1

print(minswap)
'''

cnt = 0
def merge(a, low, mid, high):
    global cnt
    l, m, k = low, mid, low
    temp = a[:]
    while l < m and m < high:
        if a[l] <= a[m]:
            temp[k] = a[l]
            l += 1
        else:
            temp[k] = a[m]
            m += 1
            cnt += mid- l
        k += 1
    if l < mid:
        temp[k:high] = a[l:mid]
    if m < high:
        temp[k:high] = a[m:high]
    a[low:high] = temp[low:high]

def merge_sort(a, l, h):
    if l == h-1:
        return
    mid = (l + h)//2
    merge_sort(a, l, mid)
    merge_sort(a, mid, h)
    merge(a, l, mid, h)

n = int(input())
a = list(map(int, input().split(' ')))
merge_sort(a,0,n)
#print(a)
print(cnt)
