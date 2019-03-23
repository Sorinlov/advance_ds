#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''
N = 100005
# 给定一个1到n的排列，依次插入到二叉树中，返回前序遍历和后序遍历
# n：如题意
# sequence：给定的排列，大小为n
# 返回值：将要输出的元素依次加入到返回值中

class node:
    def __init__(self):
        self.val = 0
        self.l = 0
        self.r = 0
    
t = [node() for i in range(N)]

root, cnt = 0, 0

#实际存储是一个线性结构，均在数组t里
#每个节点的左右子树存储的是指针，指向左右子节点在t中的下标
def insert(v, x):
    if x == 0:
        global cnt
        cnt += 1
        x = cnt
        t[x].val = v
        return x
    
    if t[x].val > v:
        t[x].l = insert(v, t[x].l)#此时传入的t[x].l为0 
    else:
        t[x].r = insert(v, t[x].r)
    
    return x

def dlr(x, ans):
    if x != 0:
        ans.append(t[x].val)
        dlr(t[x].l, ans)
        dlr(t[x].r, ans)

def lrd(x, ans):
    if x != 0:
        lrd(t[x].l, ans)
        lrd(t[x].r, ans)
        ans.append(t[x].val)
        
        
def getAnswer(n, sequence):
    global root, cnt
    
    root = cnt = 0
    
    for i in range(len(sequence)):
        root = insert(sequence[i], root)
    
    ans = []
    dlr(root, ans)
    lrd(root, ans)
    
    return ans
    ''' 请在这里设计你的算法 '''

# ================= 代码实现结束 =================

n = int(input())
sequence = list(map(int, input().split(' ')))
ans = getAnswer(n, sequence)
print(' '.join(map(str, ans[0:n])))
print(' '.join(map(str, ans[n:n+n])))
    