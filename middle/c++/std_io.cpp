#include <queue>
#include <cstdio>

using namespace std;

/* ===================== 代码实现开始 =================== */

//返回值：当前序列中位数的值
int getMedian()
{
	/* 请在这里设计你的算法 */
}

// 向当前数列末尾插入一个数x
void add(int x)
{
	/* 请在这里设计你的算法 */
}

/* ==================== 代码实现结束 ================== */

int main()
{
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= 2 * n - 1; i++) {
		int a;
		scanf("%d", &a);
		// fprintf(stderr, "%d\n", a);
		add(a);
		if (i & 1)
			printf("%d\n", getMedian());
	}
	return 0;
}