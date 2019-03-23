#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''

# 求出有多少个_a数组中的连续子序列（长度大于1），满足该子序列的最大值最小值之差不大于_d
# _n：_a数组的长度
# _d：所给d
# _a：数组_a，长度为_n
# 返回值：满足条件的连续子序列的个数


def getAnswer(n, d, a):
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            b = a[i:j+1]
            c = max(b) - min(b)
            if c <= d:
                cnt += 1
    return cnt
    ''' 请在这里设计你的算法 '''

# ================= 代码实现结束 =================

n, d = map(int, input().split())
a = list(map(int, input().split()))
print(getAnswer(n, d, a))
