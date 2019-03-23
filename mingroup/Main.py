#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''

# 将所给数组分成连续的m份，使得数字之和最大的那一份的数字之和最小
# n：数组大小
# m：题中的m
# a：所给数组，大小为n
# 返回值：最优方案中，数字之和最大的那一份的数字之和
def check(d, n, m, a):
    s = 0
    cnt = 1
    
    for i in range(n):
        if a[i] > d:
            return False
        s += a[i]
        if s > d:
            s = a[i]
            cnt += 1
    return cnt <= m

def getAnswer(n, m, a):
    l, r = 1, sum(a)
    
    while l <= r:
        mid = (l+r) >> 1
        if check(mid, n, m, a):
            r = mid - 1
        else:
            l = mid + 1
    return r + 1 
    ''' 请在这里设计你的算法 '''

# ================= 代码实现结束 =================

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(getAnswer(n, m, a))

