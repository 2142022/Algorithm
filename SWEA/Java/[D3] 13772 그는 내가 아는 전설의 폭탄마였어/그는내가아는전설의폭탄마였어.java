import java.util.Scanner;

public class 그는내가아는전설의폭탄마였어 {
	// 배열의 크기
	static int N;

	// 폭탄이 미치는 범위
	static int P;

	// 2차원 배열 맵
	static int[][] map;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수
		int T = sc.nextInt();

		// T개의 테스트케이스
		for (int t = 1; t <= T; t++) {
			// 배열의 크기
			N = sc.nextInt();

			// 폭탄이 미치는 범위
			P = sc.nextInt();

			// 2차원 배열 맵
			map = new int[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					map[i][j] = sc.nextInt();
				}
			}

			// 최대 행복 = +방향의 최대값과 x방향의 최대값의 최대값
			int happy = Math.max(plus(), xCross());

			System.out.printf("#%d %d\n", t, happy);
		}
	}

	// +방향의 최대값
	private static int plus() {
		// 리턴할 최대값
		int max = 0;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				// 현재 위치에서의 합
				int result = map[i][j];

				// 주어진 범위만큼 값 더하기
				for (int d = 1; d <= P; d++) {

					// 상
					if (i - d >= 0) {
						result += map[i - d][j];
					}

					// 하
					if (i + d < N) {
						result += map[i + d][j];
					}

					// 좌
					if (j - d >= 0) {
						result += map[i][j - d];
					}

					// 우
					if (j + d < N) {
						result += map[i][j + d];
					}
				}

				// 현재 위치에서의 값과 max값 비교
				max = Math.max(max, result);
			}
		}

		return max;
	}

	// x방향의 최대값 구하기
	private static int xCross() {
		// 리턴할 최대값
		int max = 0;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				// 현재 위치에서의 합
				int result = map[i][j];

				// 주어진 범위만큼 값 더하기
				for (int d = 1; d <= P; d++) {

					// 왼쪽 위
					if (i - d >= 0 && j - d >= 0) {
						result += map[i - d][j - d];
					}

					// 오른쪽 위
					if (i - d >= 0 && j + d < N) {
						result += map[i - d][j + d];
					}

					// 왼쪽 아래
					if (i + d < N && j - d >= 0) {
						result += map[i + d][j - d];
					}

					// 오른쪽 아래
					if (i + d < N && j + d < N) {
						result += map[i + d][j + d];
					}
				}

				// 현재 위치에서의 값과 max값 비교
				max = Math.max(max, result);
			}
		}

		return max;
	}

}
