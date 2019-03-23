#!/usr/bin/env python3

# ================= 代码实现开始 =================
N = 300005

Father = [0 for i in range(N)]
Rank = [0 for i in range(N)]

def find(x):
    global Father
    if x == Father[x]:
        return x
    Father[x] = find(Father[x])
    return Father

''' 请在这里定义你需要的全局变量 '''

# 给定n个变量以及m个约束，判定是否能找出一种赋值方案满足这m个约束条件
# n：如题意
# m：如题意
# A：大小为m的数组，表示m条约束中的a
# B：大小为m的数组，表示m条约束中的b
# E：大小为m的数组，表示m条约束中的e
# 返回值：若能找出一种方案，返回"Yes"；否则返回"No"（不包括引号）。
def getAnswer(n, m, A, B, E):
    global Father, Rank
    
    for i in range(1, n+1):
        Father[i] = i
        Rank[i] = 0
    
    cnt = 0
    for i in range(m):
        if E[i] == 1:
            E[i], E[cnt] = E[cnt], E[i]
            A[i], A[cnt] = A[cnt], A[i]
            B[i], B[cnt] = B[cnt], B[i]
            cnt += 1
            
    for i in range(m):
        setA = find(A[i])
        setB = find(B[i])
        if E[i] == 0:
            if setA == setB:
                return 'No'
        else:
            if setA != setB:
                Father[setA] = setB
    return 'Yes'


# ================= 代码实现结束 =================

T = int(input())
for _ in range(T):
    n, m = map(int, input().split(' '))
    A, B, E = [], [], []
    for i in range(m):
        a, b, e = map(int, input().split(' '))
        A.append(a)
        B.append(b)
        E.append(e)
    print(getAnswer(n, m, A, B, E))
