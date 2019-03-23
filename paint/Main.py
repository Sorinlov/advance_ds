#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''
N = 21
mo = 23333
# n辆车，m种油漆，第i种油漆够涂ai辆车，同时所有油漆恰好能涂完n辆车。若任意两辆相邻的车颜色不能相同，有多少种涂油漆的方案
# m：如题
# a：长度为m的数组，意义如题
# 返回值：方案数
def dp(a, b, c, d, e, last):
    global f
    if a | b | c | d | e == 0:
        return 1
    if f[a][b][c][d][e][last] != -1:
        return f[a][b][c][d][e][last]
    
    ret = 0
    
    if a:
        ret += dp(a - 1, b, c, d, e, 1) * (a - (last == 2))
    if b:
        

def getAnswer(m, a):
    global f
    f = [[[[[[-1 for i in range(6)] for i in range(N)] for i in range(N)] for i in range(N)] for i in range(N)] for i in range(N)]
    
    b = [0 for i in range(6)]
    
    for i in range(m):
        b[a[i]] += 1
    return dp(b[1], b[2], b[3], b[4], b[5], 0)
        
    ''' 请在这里设计你的算法 '''

# ================= 代码实现结束 =================

m = int(input())
a = list(map(int, input().split()))
print(getAnswer(m, a))
