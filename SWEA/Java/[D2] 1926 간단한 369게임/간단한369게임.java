import java.util.Scanner;

public class 간단한369게임 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();

		int N = sc.nextInt();

		for (int n = 1; n <= N; n++) {
			// 3, 6, 9의 개수
			int cnt = 0;

			int tmp = n;
			while (tmp > 0) {
				if (tmp % 10 == 3 || tmp % 10 == 6 || tmp % 10 == 9) {
					cnt++;
				}

				tmp /= 10;
			}

			if (cnt == 0) {
				System.out.print(n);
			} else if (cnt == 1) {
				System.out.print("-");
			} else if (cnt == 2) {
				System.out.print("--");
			} else if (cnt == 3) {
				System.out.print("---");
			}

			System.out.print(" ");
		}
	}
}
