#!/usr/bin/env python3

# ================= 代码实现开始 =================

N = 300005

# 用于存储一个二维平面上的点
class ip:
    
    # 构造函数
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # 先比较x轴，再比较y轴
    def __lt__ (self, other):
        return self.y < other.y if self.x == other.x else self.x < other.x

a = [ip(0, 0) for i in range(N)]
b = [ip(0, 0) for i in range(N)]

# 计算x的平方
def sqr(x):
    return x * x

# 计算点a和点b的距离
def dis(a, b):
    return (sqr(a.x - b.x) + sqr(a.y - b.y)) ** 0.5

''' 请在这里定义你需要的全局变量 '''

# 计算最近点对的距离
# n：n个点
# X, Y：分别表示x轴坐标和y轴坐标，下标从0开始
# 返回值：最近的距离
def getAnswer(n, X, Y):
    mindis = float('inf')
    for i in range(n-1):
        for j in range(i+1, n):
            dis = (sqr(X[i] - X[j]) + sqr(Y[i] - Y[j])) ** 0.5
            if dis < mindis:
                mindis = dis
    return mindis
    ''' 请在这里设计你的算法 '''

# ================= 代码实现结束 =================

n = int(input())
X = []
Y = []
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
print("{:.2f}".format(getAnswer(n, X, Y)))

