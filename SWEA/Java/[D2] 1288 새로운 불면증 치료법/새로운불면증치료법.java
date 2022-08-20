import java.util.Scanner;

public class 새로운불면증치료법 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 첫 번째 숫자
			int N = sc.nextInt();

			// 0 ~ 9까지 한 번씩 나오면 flag에 +1
			int[] flag = new int[10];

			int cnt = 0;
			// 0 ~ 9까지 한 번씩 보면 끝
			while (!check(flag)) {
				cnt++;
				int tmp = N * cnt;

				// 끝 자리 수부터 flag++
				while (tmp > 0) {
					flag[tmp % 10]++;
					tmp /= 10;
				}
			}

			// 출력
			System.out.printf("#%d %d\n", t, cnt * N);
		}
	}

	// 0 ~ 9까지 한 번씩 보면 true, 아니면 false
	static boolean check(int[] flag) {
		for (int i = 0; i < 10; i++) {
			if (flag[i] == 0) {
				return false;
			}
		}

		return true;
	}
}
