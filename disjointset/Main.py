#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''

# 给定n个变量以及m个约束，判定是否能找出一种赋值方案满足这m个约束条件
# n：如题意
# m：如题意
# A：大小为m的数组，表示m条约束中的a
# B：大小为m的数组，表示m条约束中的b
# E：大小为m的数组，表示m条约束中的e
# 返回值：若能找出一种方案，返回"Yes"；否则返回"No"（不包括引号）。
def getAnswer(n, m, A, B, E):
    cnt = 0
    for i in range(m):
        if E[i] == 1:
            E[i], E[cnt] = E[cnt], E[i]
            A[i], A[cnt] = A[cnt], A[i]
            B[i], B[cnt] = B[cnt], B[i]
            cnt += 1
            
    ID = [i for i in range(0, n+1)]
    for i in range(m):
        if E[i] == 1:
            ida = ID[A[i]]
            idb = ID[B[i]]
            for c in range(1, n+1):
                if ID[c] == ida or ID[c] == idb:
                    ID[c] = ida
        elif E[i] == 0:
            if ID[A[i]] == ID[B[i]]:
                return 'No'
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
