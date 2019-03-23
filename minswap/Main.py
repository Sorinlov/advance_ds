#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''

# 这个函数的功能是计算答案（即最少花费的金钱）
# n：表示序列长度
# a：存储整个序列 a
# 返回值：最少花费的金钱（需要注意，返回值的类型为 64 位有符号整数）
seq, seqtemp = [], []
cnt = 0

def mergesort(l, r):
    global seq, cnt, seqtemp
    if l == r:
        return
    mid = (l+r) >> 1
    mergesort(l, mid)
    mergesort(mid + 1, r)
    p, q = l, mid + 1

    for i in range(l, r+1):
        if (q > r or p <= mid and seq[p] <= seq[q]):
            seqtemp[i] = seq[p]
            p += 1
        elif q <= r:
            seqtemp[i] = seq[q]
            q += 1 
            cnt += mid - p + 1
    for i in range(l, r+1):
        seq[i] = seqtemp[i]
    
def getAnswer(n, a):
    global seq, cnt, seqtemp
    seq = list(a)
    seqtemp = [0 for i in range(n)]
    cnt = 0
    mergesort(0, n-1)
    return  cnt
    ''' 请在这里设计你的算法 '''

# ================= 代码实现结束 =================

n = int(input())
a = list(map(int, input().split()))
print(getAnswer(n, a))
