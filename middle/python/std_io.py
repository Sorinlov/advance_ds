#!/usr/bin/env python3

''' ================ 代码实现开始 ============== '''


#向当前数列末尾插入一个数a
def add(a):
	# 请在这里设计你的算法
	pass

#返回值：当前序列中位数的值
def getMedian():
	# 请在这里设计你的算法
	pass
			
''' ================ 代码实现结束 ============== '''

if __name__ == '__main__':
	n = int(input())
	a = input().split(' ')
	for i in range(2 * n - 1):
		x = int(a[i])
		add(x)
		if i % 2 == 0:
			print(getMedian())
