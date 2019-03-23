#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''
mod = 1000003
table = [[] for i in range(mod)]

def hash(x):
    return x % mod

# 执行操作时会调用这个函数
# op：对应该次操作的 op（具体请见题目描述）
# x：对应该次操作的 x（具体请见题目描述）
# 返回值：如果输出为"Succeeded"，则这个函数返回 1，否则返回 0
def check(op, x):
    h = hash(x)
    
    p = -1
    for i in range(len(table[h])):
        if x == table[h][i]:
            p = i
            break
    if op == 1:
        if p == -1:
            table[h].append(x)
            return 1
        return 0
    else:
        if p != -1:
            table[h][p] = table[h][-1]
            table[h].pop()
            return 1
        return 0
    ''' 请在这里设计你的算法 '''

# ================= 代码实现结束 =================

Q = int(input())
for _ in range(Q):
    op, x = map(int, input().split())
    print("Succeeded" if check(op, x) else "Failed")