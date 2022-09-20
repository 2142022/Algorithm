import java.util.Scanner;

public class 햄버거다이어트_DP {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 재료의 수
			int N = sc.nextInt();

			// 제한 칼로리
			int L = sc.nextInt();

			int[][] dp = new int[N + 1][L + 1];

			for (int i = 1; i < N + 1; i++) {
				// 재료의 점수
				int s = sc.nextInt();
				// 재료의 칼로리
				int k = sc.nextInt();

				for (int j = 1; j < L + 1; j++) {
					// 칼로리보다 작은 인덱스에서는 이전 값과 동일하게 채우기
					if (j < k) {
						dp[i][j] = dp[i - 1][j];
					}

					// 그 외는 최대값 비교
					else {
						dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - k] + s);
					}
				}
			}

			System.out.printf("#%d %d\n", t, dp[N][L]);
		}
	}
}
