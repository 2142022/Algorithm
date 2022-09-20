import java.util.Scanner;

public class 햄버거다이어트_비트마스킹 {
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

			// 재료에 대한 점수와 칼로리
			int[][] ingredient = new int[N][2];
			for (int i = 0; i < N; i++) {
				ingredient[i][0] = sc.nextInt();
				ingredient[i][1] = sc.nextInt();
			}

			// 최대 점수
			int max = 0;

			// 재료의 모든 경우의 수
			for (int i = 0; i < (1 << N); i++) {
				// 재료의 점수 합
				int score = 0;
				// 재료의 칼로리 합
				int kcal = 0;

				for (int j = 0; j < N; j++) {
					if ((i & (1 << j)) > 0) {
						score += ingredient[j][0];
						kcal += ingredient[j][1];
					}
				}

				// 제한 칼로리를 넘지 않는다면 max값과 비교
				if (kcal <= L) {
					max = Math.max(max, score);
				}
			}

			// 출력
			System.out.printf("#%d %d\n", t, max);
		}
	}
}