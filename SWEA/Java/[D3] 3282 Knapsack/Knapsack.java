import java.util.Scanner;

public class Knapsack {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 물건의 개수
			int N = sc.nextInt();

			// 가방의 부피
			int K = sc.nextInt();

			// 물건의 부피
			int[] V = new int[N];

			// 물건의 가치
			int[] C = new int[N];
			for (int i = 0; i < N; i++) {
				V[i] = sc.nextInt();
				C[i] = sc.nextInt();
			}

			// 부피가 i일때 최대 가치
			int[][] value = new int[2][K + 1];
			for (int i = 0; i < N; i++) {
				for (int j = 1; j < K + 1; j++) {
					// 현재 비교하는 물건(i번째 물건)의 부피보다 클 때만 생각
					if (j >= V[i]) {
						// i번째 물건을 넣지 않았을 때와 i번째 물건을 넣은 경우 최대값 비교
						value[1][j] = Math.max(value[0][j], value[0][j - V[i]] + C[i]);
					}

					// 그 외는 이전 값 복사
					else {
						value[1][j] = value[0][j];
					}
				}

				// value[0]을 value[1]로 바꾸기 (for 공간 절약)
				for (int j = 0; j < K + 1; j++) {
					value[0][j] = value[1][j];
				}
			}

			System.out.printf("#%d %d\n", t, value[1][K]);
		}
	}
}
