import java.util.Scanner;

public class 장훈이의높은선반 {

	// 점원의 수
	static int N;

	// 선반의 높이
	static int B;

	// 점원들의 키
	static int[] height;

	// 가장 큰 탑의 높이
	static int max;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 점원의 수
			N = sc.nextInt();

			// 선반의 높이
			B = sc.nextInt();

			// 점원들의 키
			height = new int[N];
			for (int i = 0; i < N; i++) {
				height[i] = sc.nextInt();
			}

			// 가장 큰 탑의 높이
			max = 2147483647;

			getSum(0, 0);

			System.out.printf("#%d %d\n", t, max - B);
		}
	}

	// 인자: idx번째 직원의 키 더하기, 현재까지 더한 직원들 키의 합
	private static void getSum(int idx, int sum) {
		// 모든 직원들을 더했으면 끝내기
		if (idx == N) {
			if (sum >= B) {
				max = Math.min(max, sum);
			}
			return;
		}

		// 선반의 높이보다 크면서 현재의 max보다 큰 값은 필요 없음
		if (!((sum >= B) && (sum > max))) {

			// 현재 직원의 키를 더하는 경우
			getSum(idx + 1, sum + height[idx]);

			// 현재 직원의 키를 더하지 않는 경우
			getSum(idx + 1, sum);
		}
	}
}
