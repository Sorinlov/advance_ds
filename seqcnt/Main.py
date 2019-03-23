#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''
N = 300005
# 求出有多少个_a数组中的连续子序列（长度大于1），满足该子序列的最大值最小值之差不大于_d
# _n：_a数组的长度
# _d：所给d
# _a：数组_a，长度为_n
# 返回值：满足条件的连续子序列的个数
n, d, max_value, min_value = 0, 0, [0 for i in range(N)], [0 for i in range(N)]
a = []

def solve(l, r):
    if l == r:
        return 0
    mid = (l + r) >> 1
    ans = solve(l, mid) + solve(mid, r)
    
    for i in range(mid + 1, r + 1):
        min_value[i] = a[i] if i == mid + 1 else min(min_value[i - 1], a[i])
        max_value[i] = a[i] if i == mid + 1 else max(max_value[i - 1], a[i])
    
    mn, mx, pos = 0, 0, r
    i = mid
    while i >= 1 and pos > mid:
        
def getAnswer(_n, _d, _a):
    
    global n, d, a
    n = _n
    d = _d
    a = _a
    return solve(0, n - 1)
''' 请在这里设计你的算法 '''

# ================= 代码实现结束 =================

n, d = map(int, input().split())
a = list(map(int, input().split()))
print(getAnswer(n, d, a))
