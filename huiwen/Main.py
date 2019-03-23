#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''

# 计算Str中有多少个回文子串
# 返回值：子串的数目
def check(s):
    if s[::-1] == s:
        return True
    return False

def getAnswer(Str):
    cnt = 0
    for l in range(1, len(Str)+1):
        for i in range(len(Str)-l+1):
            if check(Str[i:i+l]):
                cnt += 1
    return cnt
    ''' 请在这里设计你的算法 '''

# ================= 代码实现结束 =================

print(getAnswer(input()))
