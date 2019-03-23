#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''

# 本函数传入数组 a 及所有询问，你需要求解所有询问并一并返回
# n：序列 a 的长度
# a：存储了序列 a
# Q：询问个数
# query：依次存储了所有询问的参数 x
# 返回值：一个 list，依次存放各询问的答案
def quicksort(a, l ,r):
    if l >= r: return
    i, j = l, r
    pivot = a[i]
    while i < j:
        while i < j and a[j] >= pivot:
            j -= 1
        if i < j:
            a[i] = a[j]
            i += 1
        while i < j and a[i] <= pivot:
            i += 1
        if i < j:
            a[j] = a[i] 
            j -= 1
    a[i] = pivot
    quicksort(a, l, i-1)
    quicksort(a, i+1, r)

def binsearch(a, x):
    low, high = 0, len(a)-1
    
    while low <= high:
        mid = (low + high) >> 1
        if x > a[mid]:
            low = mid+1
        elif x < a[mid]:
            high = mid-1
        else:
            return a[mid]
    if low >= len(a):
        return -1
    else:
        if a[low] >= x:
            return a[low]
        elif a[low+1] >= x:
            return a[low+1]
        else:
            return a[low+2]
        
def getAnswer(n, a, Q, query):
    quicksort(a, 0, n-1)
    result = []
    for x in query:
        result.append(binsearch(a, x))
    return result
    ''' 请在这里设计你的算法 '''

# ================= 代码实现结束 =================

query = []
n = int(input())
a = list(map(int, input().split()))
Q = int(input())
for i in range(Q):
    query.append(int(input()))
for i in getAnswer(n, a, Q, query):
    print(i)
