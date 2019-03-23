import java.util.Scanner;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Std {

	// =============== 代码实现开始 ====================//

	//向当前序列的末尾添加一个数a
	private static void add(int a) {
		/* 请在这里设计你的算法 */
	}

	//返回值：当前序列的中位数
	private static int getMedian() {
		/* 请在这里设计你的算法 */
	}

	//==========================  代码实现结束  ========================= //

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		for (int i = 1; i <= 2 * n - 1; i++) {
			int a = scanner.nextInt();
			add(a);
			if (i % 2 == 1)
				System.out.println(getMedian());
		}
		scanner.close();
	}
}